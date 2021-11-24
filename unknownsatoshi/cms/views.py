from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth import login

from django.http import HttpResponse
from .models import Cms, Course, Product, Blog
from .forms import CmsForm, CourseForm, ProductForm, BlogForm

from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_user,admin_only


#admin login view
def logoutadmin(request):
    logout(request)
    return redirect('home')


def adminlog(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Adminlogin.objects.create(name=user.username, created_by=user)
            return redirect('adminhistory')
    else:
        form = UserCreationForm()
    return render(request, 'cms/admin-login.html', {'form': form})


#admin views for trade history
@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def adminpanel(request):
    return render(request, 'cms/admin-index.html')


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def adminhistory(request):
    template_name = 'cms/admin-history/index.html'
    cms = Cms.objects.all()
    context = {'cms':cms}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def trade(request, pk):
    template_name = 'cms/admin-history/edit.html'
    tradeobj = Cms.objects.get(id=pk)
    context = {'tradeobj:', tradeobj}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def createTrade(request):
    template_name = 'cms/admin-history/createhistory.html'
    form = CmsForm
    if request.method == 'POST':
        form = CmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhistory')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def updateTrade(request, pk):
    template_name = 'cms/admin-history/createhistory.html'
    trade = Cms.objects.get(id=pk)
    form = CmsForm(instance=trade)

    if request.method == 'POST':
        form = CmsForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('adminhistory')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def deleteTrade(request, pk):
    template_name = 'cms/admin-history/edit.html'
    trade = Cms.objects.get(id=pk)
    if request.method == 'POST':
        trade.delete()
        return redirect('adminhistory')
    context = {'trade': trade}
    return render(request, template_name, context)


#admin views for courses
@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admincourse(request):
    template_name = 'cms/admin-course/index.html'
    courses_field = Course.objects.all()
    context = {'courses_field':courses_field}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def updateCourse(request, pk):
    template_name = 'cms/admin-course/create.html'
    info = Course.objects.get(id=pk)
    form = CourseForm(instance=info)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES,instance=info)
        if form.is_valid():
            form.save()
            return redirect('admincourse')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def createCourse(request):
    template_name = 'cms/admin-course/create.html'
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admincourse')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def deleteCourse(request, pk):
    template_name = 'cms/admin-course/edit.html'
    info = Course.objects.get(id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('admincourse')
    context = {'info': info}
    return render(request, template_name, context)


#admin views for store
@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_product(request):
    template_name = 'cms/admin-store/index.html'
    products = Product.objects.all()
    context = {'products':products}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_product(request):
    template_name = 'cms/admin-store/create.html'
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminstore')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def update_product(request, pk):
    template_name = 'cms/admin-store/create.html'
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('adminstore')
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_product(request, pk):
    template_name = 'cms/admin-store/edit.html'
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('adminstore')
    context = {'product': product}
    return render(request, template_name, context)

################################################################################

# blog views for admin
def single_blog(request):
    template_name = 'cms/single.html'
    return render(request, template_name)


def admin_blog(request):
    template_name = 'cms/admin-blog/posts/index.html'
    blogs = Blog.objects.all()
    featured_story =Blog.objects.filter(featured_stories=True)
    latest_new =Blog.objects.filter(latest_news=True)
    latest_article =Blog.objects.filter(latest_articles=True)
    context = {
        'blogs':blogs,
        'featured_story':featured_story,
        'latest_new':latest_new,
        'latest_article':latest_article,        
    }
    return render(request, template_name, context)


def create_blog(request):
    template_name = 'cms/admin-blog/posts/create.html'
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminblog')
    context = {'form':form}
    return render(request, template_name, context)


def update_blog(request, pk):
    template_name = 'cms/admin-blog/posts/create.html'
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('adminblog')
    context = {'form':form}
    return render(request, template_name, context)


def delete_blog(request, pk):
    template_name = 'cms/admin-blog/posts/delete.html'
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('adminblog')
    context = {'blog': blog}
    return render(request, template_name, context)


#normal pages for users views
def home(request):
    return render(request, 'cms/index.html')


def about(request):
    template_name = 'cms/about.html'
    return render(request, template_name)


def contact(request):
    template_name = "cms/contact.html"
    return render(request, template_name)


def register(request):
    template_name = 'cms/register.html'
    return render(request, template_name)
    

def login(request):
    template_name = 'cms/login.html'
    return render(request, template_name)


def courses(request):
    template_name = 'cms/course.html'
    courses_field = Course.objects.all()
    context = {'courses_field':courses_field}
    return render(request, template_name, context)


def trade_history(request):
    template_name = 'cms/trade.html'
    cmss = Cms.objects.all()
    context = {'cmss':cmss}
    return render(request, template_name,context)


def onlinestore(request):
    template_name = 'cms/store.html'
    products = Product.objects.all()
    context = {'products':products}
    return render(request, template_name, context)


# blog list
def blog(request):
    template_name = 'cms/blog.html'
    blogs = Blog.objects.all()
    featured_story =Blog.objects.filter(featured_stories=True)
    latest_new =Blog.objects.filter(latest_news=True)
    latest_article =Blog.objects.filter(latest_articles=True)
    context = {
        'blogs':blogs,
        'featured_story':featured_story,
        'latest_new':latest_new,
        'latest_article':latest_article,
    }
    return render(request, template_name, context)


# blog details
def blog_detail(request, pk):
    template_name = 'cms/single.html'
    blog = Blog.objects.get(id=pk)
    context = {'blog': blog}
    return render(request, template_name, context)


# faq page
def faqs(request):
    template_name = 'cms/faqs.html'
    return render(request, template_name)


#authentication page
def Auth(request):
    template_name = 'cms/auth.html'
    return render(request, template_name)


#premium subscription page
def premium_subscription(request):
    template_name = "cms/subscription.html"
    return render(request, template_name)
