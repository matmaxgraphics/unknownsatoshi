from .models import *
from .forms import *
from django.contrib import messages
from userprolog.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import get_object_or_404, render, redirect
from .decorators import unauthenticated_user, allowed_user, admin_only


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
            return redirect("admin-history")
        return redirect("admin-login")
    return render(request, template_name)


#admin logout
def admin_logout(request):
    logout(request)
    return redirect("admin-login")

#admin views for trade history
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admin_panel(request):
    template_name = 'cms/admin-index.html'
    return render(request, template_name)


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
    form = CmsForm
    if request.method == 'POST':
        form = CmsForm(request.POST)
        if form.is_valid():
            trade = form.save()
            messages.success(request, f"{trade.title} added")
            return redirect('admin-history')
        else:
            form = CmsForm(request.POST)
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
            return redirect('admin-history')
        messages.info(request, f"unable to update, try again")
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
def update_course(request, pk):
    template_name = 'cms/admin-course/create.html'
    course = Course.objects.get(id=pk)
    form = CourseForm(request.POST)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES,instance=course)
        if form.is_valid():
            form.save()
            return redirect('admin-course')
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
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-course')
    context = {'form':form}
    return render(request, template_name, context)


# admin delete course
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_course(request, pk):
    template_name = 'cms/admin-course/edit.html'
    info = Course.objects.get(id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('admin-course')
    context = {'info': info}
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
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminstore')
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
            return redirect('admin-product')
        form = ProductUpdateForm(instance=product)
    context = {'form':form}
    return render(request, template_name, context)


@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def delete_product(request, id):
    template_name = 'cms/admin-store/delete.html'
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
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
    context = {
        'blogs':blogs,     
    }
    return render(request, template_name, context)


# admin create blog
@login_required(login_url='admin-login')
@allowed_user(allowed_roles=['admin'])
@admin_only
def create_blog(request):
    template_name = 'cms/admin-blog/create.html'
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('admin-blog')
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
        
        messages.info(request, f"Unable to update post, try again")
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
        messages.success(request, f"Unable to delete post, try again")
        return render(request, template_name)


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
            messages.success(request, f" successfully created")
            return redirect('admin-user-list')
        messages.info(request, f"Unable to create user, please try again")
        return redirect("admin-create-user")
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
    form = UserUpdateForm()
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"User updated successfully")
            return redirect("admin-user-list")
        messages.info(request, f"unable to update user")
        return redirect("admin-update-user", id)
    else:
        form = UserUpdateForm(instance=user)
    context = {"form":form}
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
        messages.info(request, f"unable to delete user")
        return render(request, template_name)
    

#normal pages for users views
def home(request):
    template_name = 'cms/index.html'
    return render(request, template_name)


def about(request):
    template_name = 'cms/about.html'
    return render(request, template_name)


def contact(request):
    template_name = "cms/contact.html"
    return render(request, template_name)


def courses(request):
    template_name = 'cms/course.html'
    courses = Course.objects.all()
    context = {'courses':courses}
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


# premium subscription list page
def plan_list(request):
    template_name = "cms/subscription.html"
    plans = Plan.objects.all()
    context = {"plans":plans}
    return render(request, template_name, context)

def plan_details(request, id):
    template_name = "cms/subscription.html"
    plan = get_object_or_404(Plan, id=id)
    context = {"plan":plan}
    return render(request, template_name, context)


# monthly subscription
def monthly_subscription_checkout(request,id):
    plan_id = get_object_or_404(Plan, id=id)
    plan = Plan.objects.filter(id=plan_id, title="monthly plan")
    

# quarterly subscription
def quarterly_subscription_checkout(request,id):
    plan_id = get_object_or_404(Plan, id=id)
    plan = Plan.objects.filter(id=plan_id, title="quarterly plan")


# yearly subscription
def yearly_subscription_checkout(request,id):
    plan_id = get_object_or_404(Plan, id=id)
    plan = Plan.objects.filter(id=plan_id, title="yearly plan")
