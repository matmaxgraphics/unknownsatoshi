import math
import time
import random
import decimal
import requests
from .forms import *
from .models import *
from userprolog.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date, datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from cms.mailing_helper import UserRegisterationNotification, UserSubscriptionNotification
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .decorators import unauthenticated_user, allowed_user, admin_only
from unknownsatoshi.settings import FLW_PRODUCTION_SECRET_KEY, FLW_SANDBOX_SECRET_KEY
from django.template.loader import render_to_string
from unknownsatoshi.settings import DEFAULT_FROM_EMAIL, CONTACT_EMAIL
import json

# from hitcount.views import HitCountDetailView



@unauthenticated_user
def admin_login(request):
    template_name = "cms/admin-login.html"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            messages.success(request, f"Welcome {user.username}")
            return redirect("admin-history")
        messages.error(request, f"Login attempt failed, please try again")
        return redirect("admin-login")
    return render(request, template_name)


#admin logout
def admin_logout(request):
    logout(request)
    messages.success(request, f"Logout  Successful")
    return redirect("home")


# admin history view
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_history(request):
    template_name = 'cms/admin-history/index.html'
    cms = Cms.objects.all()
    context = {'cms':cms}
    return render(request, template_name, context)


# admin update trade history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def trade(request, pk):
    template_name = 'cms/admin-history/edit.html'
    tradeobj = Cms.objects.get(id=pk)
    context = {'tradeobj:', tradeobj}
    return render(request, template_name, context)


# admin create trade history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_trade(request):
    template_name = 'cms/admin-history/createhistory.html'
    form = CmsForm()
    if request.method == 'POST':
        form = CmsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{form.instance.title} added")
            return redirect('admin-history')
        messages.error(request, f"Unable to create trade, please try again")
        return redirect("create-trade")
    else:
        form = CmsForm()
    context = {'form':form}
    return render(request, template_name, context)


# admin update trade history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def update_trade(request, pk):
    template_name = 'cms/admin-history/edit.html'
    trade = Cms.objects.get(id=pk)
    form = CmsForm(request.POST, instance=trade)
    if request.method == 'POST':
        form = CmsForm(request.POST, request.FILES, instance=trade)
        if form.is_valid():
            form.save()
            messages.success(request, f"Trade updated successfully")
            return redirect('admin-history')
        messages.error(request, f"Unable to update trade, Try again")
        return redirect('update-trade', pk)
    else:
        form = CmsForm(instance=trade)
    context = {"form":form}
    return render(request, template_name, context)
    

# admin delete trade history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_trade(request, pk):
    template_name = 'cms/admin-history/delete_history.html'
    trade = Cms.objects.get(id=pk)
    if request.method == 'POST':
        trade.delete()
        messages.success(request,f"Trade deleted")
        return redirect('admin-history')
    context = {'trade': trade}
    return render(request, template_name, context)


# admin views for courses
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_course(request):
    template_name = 'cms/admin-course/index.html'
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, template_name, context)


# admin update course
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def update_course(request, id):
    template_name = 'cms/admin-course/edit.html'
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, f"Course updated")
            return redirect('admin-course')
        messages.error(request, f"unable to update course, Try again")
        return redirect("update-course", id)
    else:
        form = CourseForm(instance=course)
    context = {'form':form}
    return render(request, template_name, context)


# admin create course
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_course(request):
    template_name = 'cms/admin-course/create.html'
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Course created successfully")
            return redirect('admin-course')
        messages.error(request, f"Unable to create course, Try again")
        return redirect("reate-course")
    context = {'form':form}
    return render(request, template_name, context)


# admin delete course
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_course(request, pk):
    template_name = 'cms/admin-course/delete.html'
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, f"Course deleted successfully")
        return redirect('admin-course')
    context = {'course': course}
    return render(request, template_name, context)


#admin views for store
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_product(request):
    template_name = 'cms/admin-store/index.html'
    products = Product.objects.all()
    context = {'products':products}
    return render(request, template_name, context)


# admin create product
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_product(request):
    template_name = 'cms/admin-store/create.html'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product created successfully")
            return redirect('admin-product')
        messages.error(request, f"Unable to create product, Try again")
        return redirect("create-product")
    else:
        form = ProductForm(request.POST, request.FILES)
    context = {'form':form}
    return render(request, template_name, context)


# admin update product
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def update_product(request, id):
    template_name = 'cms/admin-store/edit.html'
    product = get_object_or_404(Product, id=id)
    form = ProductUpdateForm(instance=product)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Product updated successfully")
            return redirect('admin-product')
        messages.error(request, f"Unable to update product, Try again")
        return redirect("update-product", id)
    else:
        form = ProductUpdateForm(instance=product)
    context = {'form':form}
    return render(request, template_name, context)


# admin can delete products
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_product(request, id):
    template_name = 'cms/admin-store/delete.html'
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, f"product successfully deleted")
        return redirect('admin-product')
    context = {'product': product}
    return render(request, template_name, context)


# admin blog list
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_blog(request):
    template_name = 'cms/admin-blog/index.html'
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, template_name, context)


# admin can create posts
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_blog(request):
    template_name = 'cms/admin-blog/create.html'
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            messages.success(request, f"Post created successfully")
            return redirect('admin-blog')
        messages.error(request, f"Unable to create Post, Try again")
        return redirect("create-blog")
    else:
        form = BlogForm(request.POST, request.FILES)
    context = {'form':form}
    return render(request, template_name, context)


#admin update blog
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def update_blog(request, pk):
    template_name = 'cms/admin-blog/edit.html'
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, f"Post updated successfully")
            return redirect('admin-blog')
        messages.error(request, f"Unable to update post, try again")
        form = BlogForm(request.POST, request.FILES, instance=blog)
    else:
        form = BlogForm(instance=blog)
    context = {'form':form}
    return render(request, template_name, context)


#admin delete blog
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_blog(request, pk):
    template_name = 'cms/admin-blog/delete.html'
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, f"Post deleted successfully")
        return redirect('admin-blog')
    else:
        context = {"blog":blog}
        return render(request, template_name, context)


#admin create user
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_create_user(request):
    template_name = 'cms/admin-user/create_user.html'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = False
            user.is_superuser = False
            user.save()
            messages.success(request, f" Account for {user.email} successfully created")
            return redirect('admin-user-list')
        messages.error(request, f"Unable to create user, please try again")
        return redirect("admin-create-user")
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, template_name, context)


# admin users list
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_user_list(request):
    template_name = "cms/admin-user/index.html"
    users = User.objects.all()
    context = {"users":users}
    return render(request, template_name, context)


#admin update users
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_update_user(request, id):
    template_name = "cms/admin-user/edit.html"
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"User updated successfully")
            return redirect("admin-user-list")
        messages.error(request, f"Unable to update user")
        return redirect("admin-update-user", id)
    else:
        form = UserUpdateForm(instance=user)
    context = {"form":form, "user":user}
    return render(request, template_name, context)


#admin delete users
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_delete_user(request, id):
    template_name = 'cms/admin-user/delete.html'
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f"User deleted successfully")
        return redirect('admin-user-list')
    else:
        context = {"user":user}
        return render(request, template_name, context)


# admin create first time plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_create_first_time_plan(request):
    template_name = 'cms/admin-plan-first/create.html'
    form = FirstTimePlanForm()
    if request.method == 'POST':
        form = FirstTimePlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"First Time Plan created successfully")
            return redirect('admin-product')
        messages.error(request, f"Unable to create first time plan, Try again")
        return redirect("create_first_time_plan")
    else:
        form = FirstTimePlanForm(request.POST)
    context = {'form':form}
    return render(request, template_name, context)


#admin views for first time plan list
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_first_time_plan_list(request):
    template_name = 'cms/admin-plan-first/index.html'
    first_time_plans = FirstTimePlan.objects.all()
    context = {"first_time_plans": first_time_plans}
    return render(request, template_name, context)


# admin update first time plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_update_first_time_plan(request, slug):
    template_name = 'cms/admin-plan-first/edit.html'
    first_time_plan = get_object_or_404(FirstTimePlan, slug=slug)
    form = FirstTimePlanUpdateForm(instance=first_time_plan)
    if request.method == 'POST':
        form = FirstTimePlanUpdateForm(request.POST, instance=first_time_plan)
        if form.is_valid():
            form.save()
            messages.success(request, f"First time plan updated successfully")
            return redirect('first_time_plan_list')
        messages.error(request, f"Unable to update first time plan, Try again")
        return redirect("update_first_time_plan", slug)
    else:
        form = FirstTimePlanUpdateForm(instance=first_time_plan)
    context = {'form': form}
    return render(request, template_name, context)


# admin can delete first time plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_delete_first_time_plan(request, slug):
    template_name = 'cms/admin-plan-first/delete.html'
    first_time_plan = get_object_or_404(FirstTimePlan, slug=slug)
    if request.method == 'POST':
        first_time_plan.delete()
        messages.success(request, f"product successfully deleted")
        return redirect('first_time_plan_list')
    context = {'first_time_plan': first_time_plan}
    return render(request, template_name, context)


# admin create plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_create_plan(request):
    template_name = 'cms/admin-plan/create.html'
    form = PlanForm()
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Plan created successfully")
            return redirect('admin-plan-list')
        messages.error(request, f"Unable to create plan")
        return redirect("admin-create-plan")
    else:
        form = PlanForm(request.POST)
    context = {'form':form}
    return render(request, template_name, context)


#admin plan list  
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_plan_list(request):
    template_name = "cms/admin-plan/index.html"
    plans = Plan.objects.all()
    context = {"plans":plans}
    return render(request, template_name, context)


#admin update plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_update_plan(request, slug):
    template_name = "cms/admin-plan/edit.html"
    plan = get_object_or_404(Plan, slug=slug)
    form = PlanForm(instance=plan)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, f"plan updated successfully")
            return redirect("admin-plan-list")
        messages.error(request, f"Unable to update user, Try again")
        return redirect("admin-update-plan", slug)
    else:
        form = PlanForm(instance=plan)
    context = {"form":form}
    return render(request, template_name, context)


# admin delete plan
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_delete_plan(request, slug):
    template_name = 'cms/admin-plan/delete.html'
    plan = get_object_or_404(Plan, slug=slug)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, f"Plan deleted successfully")
        return redirect('admin-plan-list')
    else:
        return render(request, template_name)



#admin first time  subscription history
login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_first_time_subscription_list(request):
    template_name = "cms/admin-first-time-subscription/index.html"
    first_time_subscriptions = FirstTimeSubscriptionHistory.objects.all()
    context = {"first_time_sub": first_time_subscriptions}
    return render(request, template_name, context)


#admin delete first time subscription subscription history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_delete_first_time_subscription(request, id):
    template_name = 'cms/admin-first-time-subscription/delete.html'
    first_subscription = get_object_or_404(FirstTimeSubscriptionHistory, id=id)
    if request.method == 'POST':
        first_subscription.delete()
        messages.success(request, f"subscription deleted successfully")
        return redirect("first_time_subscription_list", id)
    else:
        context = {"first_subscription":first_subscription}
        return render(request, template_name, context)


#admin subscription history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_subscription_history(request):
    template_name = "cms/admin-subscription/index.html"
    subscriptions = SubscriptionHistory.objects.all()
    context = {"subscriptions":subscriptions}
    return render(request, template_name, context)


#admin delete subscription history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_delete_subscription(request, id):
    template_name = 'cms/admin-subscription/delete.html'
    subscription = get_object_or_404(SubscriptionHistory, id=id)
    if request.method == 'POST':
        subscription.delete()
        messages.success(request, f"subscription deleted successfully")
        return redirect('admin-sub-list')
    else:
        context = {"subscription":subscription}
        return render(request, template_name, context)


# normal pages for users views
def home(request):
    template_name = 'cms/index.html'
    blogs = Blog.objects.filter(home_page=True)
    context = {"blogs":blogs}
    return render(request, template_name, context)


# about us page
def about(request):
    template_name = 'cms/about.html'
    return render(request, template_name)


def contact(request):
    template_name = "cms/contact.html"
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        subject = f"mail from {fullname}"
        message = request.POST.get("messages")
        body = {
            "message":message,
        }
        message_body = "\n".join(body.values())
        if subject and email and message and fullname:
            mail_helper = UserRegisterationNotification(
                email_subject=subject, 
                email_body=str(message_body), 
                sender_email=DEFAULT_FROM_EMAIL,
                receiver_email=CONTACT_EMAIL,
                reply_to=email,
            )
            mail_helper.mail_user()
            messages.success(request, "your message has been sent successfully")
            return redirect("home")
        messages.error(request, f"something went wrong, please try again")
        return redirect("contact")
    else:
        return render(request, template_name)


# frequently asked question page
def faq_view(request):
    template_name = "cms/faqs.html"
    return render(request, template_name)


def privacy_view(request):
    template_name = "cms/privacy.html"
    return render(request, template_name)


def courses(request):
    template_name = 'cms/course.html'
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, template_name, context)


# trade history page
def trade_history(request):
    template_name = 'cms/trade.html'
    cmss = Cms.objects.all()
    context = {'cmss':cmss}
    return render(request, template_name, context)


# products list page
def onlinestore(request):
    template_name = 'cms/store.html'
    merch_products = Product.objects.filter(product_category__name__icontains="merch")
    nfts_products = Product.objects.filter(product_category__name__icontains="nfts")
    context = {'merch_products':merch_products, "nfts_products":nfts_products}
    return render(request, template_name, context)


# blog list
def blog(request):
    template_name = 'cms/blog.html'
    blogs = Blog.objects.all()
    featured_story = Blog.objects.filter(featured_stories=True, premium=False)
    latest_new = Blog.objects.filter(latest_news=True, premium=False)
    latest_article =Blog.objects.filter(latest_articles=True, premium=False)

    premium_featured_story = Blog.objects.filter(featured_stories=True, premium=True)
    premium_latest_new = Blog.objects.filter(latest_news=True, premium=True)
    premium_latest_article =Blog.objects.filter(latest_articles=True, premium=True)
    
    context = {
        'blogs':blogs,
        'featured_story':featured_story,
        'latest_new':latest_new,
        'latest_article':latest_article,
        "premium_featured_story":premium_featured_story,
        "premium_latest_new":premium_latest_new,
        "premium_latest_article":premium_latest_article
    }
    return render(request, template_name, context)


# regular blog details
def blog_detail(request, slug):
    template_name = 'cms/single.html'
    blog = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all()
    latest_article =Blog.objects.filter(latest_articles=True, premium=False)
    msg = False
    form = CommentForm()
    
    #views blog count
    ip=request.META['REMOTE_ADDR']
    if not ViewCount.objects.filter(blog=blog, session=request.session.session_key):
        view=ViewCount(blog=blog, ip_address=ip, session=request.session.session_key)
        
        view.save()
    blog_views=ViewCount.objects.filter(blog=blog).count()
    
    if request.user.is_authenticated:
        user = request.user

        if blog.likes.filter(id=user.id).exists():
            msg = True
    context = {'blog': blog, 'msg':msg, 'form':form, "view_count":blog_views,'blogs':blogs,'latest_article':latest_article,}

    try:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.blog = blog
            comment.owner = request.user
            comment.save()


            messages.success(request, 'Your review was successfully submitted!')
            return redirect('blog-detail', slug=blog.slug)
    
        if not request.user or not request.user.is_authenticated:
            
            return render(request, template_name, context)

        else:
            return render(request, template_name, context)
    except:
        return render(request, "cms/login-prompt.html", context)
   
#blog comments
     
#premium blog details
def premium_blog_detail(request, slug):
    template_name = 'cms/premium-single.html'
    blog = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all()
    
    premium_featured_story = Blog.objects.filter(featured_stories=True, premium=True)
    premium_latest_new = Blog.objects.filter(latest_news=True, premium=True)
    premium_latest_article =Blog.objects.filter(latest_articles=True, premium=True)
    msg = False
    form = CommentForm()
    
    #premium view blog count
    
    ip=request.META['REMOTE_ADDR']
    if not ViewCount.objects.filter(blog=blog, session=request.session.session_key):
        view=ViewCount(blog=blog, ip_address=ip, session=request.session.session_key)
        
        view.save()
    blog_views=ViewCount.objects.filter(blog=blog).count()

    if request.user.is_authenticated:
        user = request.user

        if blog.likes.filter(id=user.id).exists():
            msg = True
    context = {"blog":blog, "msg": msg, "form":form, "blog_views":blog_views,'blogs':blogs,
        "premium_featured_story":premium_featured_story,
        "premium_latest_new":premium_latest_new,
        "premium_latest_article":premium_latest_article}
    try:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            comment = form.save(commit=False)
            comment.blog = blog
            comment.owner = request.user
            comment.save()

            messages.success(request, 'Your review was successfully submitted!')
            return redirect('premium-blog-detail', slug=blog.slug)
        premium_user = SubscriptionHistory.objects.filter(user=request.user, active=True).exists()
        if request.user.is_authenticated and blog.premium and premium_user:
            return render(request, template_name, context)

        if request.user.is_authenticated and premium_user and not blog.premium:
            return render(request, template_name, context)
        
        if request.user.is_authenticated and blog.premium and not premium_user:
            return render(request, "cms/plan-notify.html")
    except:
        return render(request, "cms/login-prompt.html")

    
# faq page
def faqs(request):
    template_name = 'cms/faqs.html'
    return render(request, template_name)


#authentication page
def unauthorized_page(request):
    template_name = 'cms/auth.html'
    return render(request, template_name)


# premium subscription list page
def plan_list(request):
    template_name = "cms/subscription.html"
    plans = Plan.objects.all()
    context = {"plans":plans}
    return render(request, template_name, context)


# plan details
first_time_sub_detail = None
main_plan_detail = None
@login_required(login_url="user-login")
def plan_details(request, slug):
    template_name = "cms/plan_payment.html"
    user = request.user
    global first_time_sub_detail, main_plan_detail
    
    if FirstTimeSubscriptionHistory.objects.filter(user=user, active=True).exists():
        messages.error(request, f"you already have an active plan")
        return redirect("user-first-sub")

    first_time_sub_detail = get_object_or_404(FirstTimePlan, slug=slug)
    print(f"PLAN = {first_time_sub_detail}: {first_time_sub_detail.discount_price}")
    first_time_sub = FirstTimeSubscriptionHistory.objects.filter(user=user).exists()
    if not first_time_sub:
        messages.success(request,f"You have a discount on your first time subscription so you pay ${first_time_sub_detail.discount_price}")
        if request.method == "GET":
            user_id = str(user.id)
            plan_id= str(first_time_sub_detail)
            first_name = user.first_name
            last_name = user.last_name
            amount = first_time_sub_detail.discount_price
            email = user.email
            phone_no = user.phone_no
            plan_title = first_time_sub_detail.title
            plan_desc = first_time_sub_detail.desc
            return redirect(str(process_payment(request,user_id=user_id, plan_id=plan_id, first_name=first_name, last_name=last_name, amount=float(amount), email=email, phone_no=phone_no, plan_title=plan_title, plan_desc=plan_desc)))
    elif(first_time_sub and FirstTimeSubscriptionHistory.objects.filter(user=user, active=False).exists()):
        
        # checks if user has active plan on main subscription table
        if SubscriptionHistory.objects.filter(user=user, active=True).exists():
            messages.error(request, f"you already have an active plan")
            return redirect("user-sub-list")

        main_plan_detail = get_object_or_404(Plan, slug=slug)
        if request.method == "GET":
            user_id = str(user.id)
            plan_id= str(main_plan_detail)
            first_name = user.first_name
            last_name = user.last_name
            amount = main_plan_detail.discount_price
            email = user.email
            phone_no = user.phone_no
            plan_title = main_plan_detail.title
            plan_desc = main_plan_detail.desc
            return redirect(str(process_payment(request, user_id=user_id, plan_id=plan_id, first_name=first_name, last_name=last_name, amount=float(amount), email=email, phone_no=phone_no, plan_title=plan_title, plan_desc=plan_desc)))
        else:   
            context = {"plan":main_plan_detail, "user":user}
        return render(request, template_name, context)



amount_paid = ""
# process plan payment
@login_required(login_url="user-login")
def process_payment(request, user_id, plan_id, first_name, last_name, amount, email, phone_no, plan_title, plan_desc):
    global amount_paid
    amount_paid = amount
    name = f"{first_name} {last_name}".capitalize()
    # auth_token= FLW_PRODUCTION_SECRET_KEY
    auth_token = FLW_SANDBOX_SECRET_KEY
    header = {'Authorization': 'Bearer ' + auth_token}

    data = {
        "tx_ref":''+str(math.floor(1000000 + random.random()*9000000)),
        "plan_id":plan_id,
        "amount": amount,
        "currency":"USD",
        "redirect_url": "http://localhost:8000/callback",
        "payment_options": "card",
        "meta":{
            "consumer_id": user_id,
            "consumer_mac": "92a3-912ba-1192a"
        },
        "customer":{
            "email": email,
            "phonenumber": str(phone_no),
            "name": name
        },
        "customizations":{
            "title": plan_title,
            "description": plan_desc,
            "logo": "https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
        }
    }

    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=header)
    response=response.json()
    link=response['data']['link']
    return link


# returns subscription's transaction_id, transaction_reference and transaction_status
today = datetime.now().date()

@require_http_methods(['GET', 'POST'])
@login_required(login_url="user-login")
def payment_response(request):
    user = request.user
    amount = amount_paid
    full_name = f"{user.first_name} {user.last_name}"
    phone_no = user.phone_no
    tx_ref = request.GET.get('tx_ref' or None)
    status = request.GET.get('status' or None)
    transaction_id = request.GET.get('transaction_id' or None)
    
    # checks if user has active plan on main subscription table
    if SubscriptionHistory.objects.filter(reference=tx_ref).exists():
        messages.error(request, f"your email {user.email} has an active plan already")
        return redirect("user-sub-list")

    # checks if user has active plan on first time subscription table
    elif FirstTimeSubscriptionHistory.objects.filter(reference=tx_ref).exists():
        messages.error(request, f"your email {user.email} has an active plan already")
        return redirect("user-first-sub")
    expiry_date = today + timedelta(days=first_time_sub_detail.duration_in_days)
    print(f"PLAN {first_time_sub_detail.title}\nEXPIRY {expiry_date}")
    
    
    # checks if user already exist on the first time subscriber table
    first_time_subscriber = FirstTimeSubscriptionHistory.objects.filter(user=user)
    if not first_time_subscriber.exists():
        subscription = FirstTimeSubscriptionHistory.objects.create(
            user=user,
            email=user.email,
            full_name=full_name,
            phone_no=phone_no,
            plan=first_time_sub_detail, 
            amount_paid=amount,
            reference = tx_ref, 
            transaction_id=transaction_id,
            status=status,
            expiry_date=expiry_date,
            active=True
        )
    
    subscription = SubscriptionHistory.objects.create(
        user=user, 
        email=user.email,
        full_name=full_name,
        phone_no=phone_no,
        plan=main_plan_detail, 
        amount_paid=amount,
        reference = tx_ref, 
        transaction_id=transaction_id,
        status=status,
        expiry_date=expiry_date,
        active=True
    )
    subject = f"Plan Subscription Notification"
    message = f"{user.email} just subscribed for the {subscription.plan}"
    try:
        send_mail = UserSubscriptionNotification(
        email_subject=subject,
        email_body=message,
        sender_email=DEFAULT_FROM_EMAIL,
        receiver_email=CONTACT_EMAIL,
    )
        send_mail.mail_admin()
    except:
        messages.error(f"could not connect to smtp, redirecting to home page")
    finally:
        return redirect("home")


# newsletter subscription page
def newsletter(request):
    template_name = "base2.html"
    if request.method == "POST":
        email = request.POST.get("email")
        subject = f"Nofification for newsletter subscriber"
        message = f"{email} just subscribed for newsletter"
        
        if Newsletter.objects.filter(email=email).exists():
            time.sleep(1)
            messages.success(request, f"The email you provided already exist in our newsletter list.")
            return redirect("home")
            
        Newsletter.objects.create(email=email)
        send_mail = UserSubscriptionNotification(
            email_subject=subject,
            email_body=message,
            sender_email=DEFAULT_FROM_EMAIL,
            receiver_email=CONTACT_EMAIL,
            )
        send_mail.mail_admin()
        messages.success(request, "You have successfully been added to our newsletter subscription.")
        return redirect("home")
    else:
        return render(request, template_name)


# error page
def custom_page_not_found(request, exception):
    return render(request, "cms/404.html")


def like_post(request):
    data = json.loads(request.body)
    id = data["id"]
    blog = Blog.objects.get(id=id)
    checker = None
    
    if request.user.is_authenticated:

        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            checker = 0  
        else:
            blog.likes.add(request.user)
            checker = 1
    
    likes = blog.likes.count()
    
    info = {
        "check": checker,
        "num_of_likes": likes
    }
    
    return JsonResponse(info, safe=False)
    
