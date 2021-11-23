from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth import login

from django.http import HttpResponse
from .models import Adminlogin, Cms, Course, Store, Blog
from .forms import CmsForm, CourseForm, StoreForm, BlogForm

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
            admin =Adminlogin.objects.create(name=user.username, created_by=user)

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
    cms = Cms.objects.all()
    context = {'cms':cms}
    return render(request, 'cms/admin-history/index.html',context)


@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def trade(request, pk):
    tradeobj = Cms.objects.get(id=pk)
    print('tradeobj:', tradeobj)
    return render(request, 'cms/admin-history/edit.html', {'trade': tradeobj})

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def createTrade(request):
    form = CmsForm
    if request.method == 'POST':
        form = CmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminhistory')
    context = {'form':form}
    return render(request, 'cms/admin-history/createhistory.html', context)



@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def updateTrade(request, pk):
    trade = Cms.objects.get(id=pk)
    form = CmsForm(instance=trade)

    if request.method == 'POST':
        form = CmsForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('adminhistory')
    context = {'form':form}
    return render(request, 'cms/admin-history/createhistory.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def deleteTrade(request, pk):
    trade = Cms.objects.get(id=pk)
    if request.method == 'POST':
        trade.delete()
        print(trade)
        return redirect('adminhistory')
    context = {'trade': trade}
    return render(request, 'cms/admin-history/edit.html', context)



#admin views for courses
@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def admincourse(request):
    courses_field = Course.objects.all()
    context = {'courses_field':courses_field}
    return render(request, 'cms/admin-course/index.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def updateCourse(request, pk):
    info = Course.objects.get(id=pk)
    form = CourseForm(instance=info)

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES,instance=info)
        if form.is_valid():
            form.save()
            return redirect('admincourse')
    context = {'form':form}
    return render(request, 'cms/admin-course/create.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def createCourse(request):
    form = CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admincourse')
    context = {'form':form}
    return render(request, 'cms/admin-course/create.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def deleteCourse(request, pk):
    info = Course.objects.get(id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('admincourse')
    context = {'info': info}
    return render(request, 'cms/admin-course/edit.html', context)

#admin views for store
@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def adminStore(request):
    store_field = Store.objects.all()
    context = {'store_field':store_field}
    return render(request, 'cms/admin-store/index.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def createStore(request):
    form = StoreForm
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminstore')
    context = {'form':form}
    return render(request, 'cms/admin-store/create.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def updateStore(request, pk):
    shop = Store.objects.get(id=pk)
    form = StoreForm(instance=shop)

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES,instance=shop)
        if form.is_valid():
            form.save()
            return redirect('adminstore')
    context = {'form':form}
    return render(request, 'cms/admin-store/create.html', context)

@login_required(login_url='adminlogin')
@allowed_user(allowed_roles=['admin'])
@admin_only
def deleteStore(request, pk):
    shop = Store.objects.get(id=pk)
    if request.method == 'POST':
        shop.delete()
        return redirect('adminstore')
    context = {'shop': shop}
    return render(request, 'cms/admin-store/edit.html', context)

# blog views for admin
def singleBlog(request):
    return render(request, 'cms/single.html')

def adminblog(request):
    blogs = Blog.objects.all()
    featured_story =Blog.objects.filter(featured_stories=True)
    latest_new =Blog.objects.filter(latest_news=True)
    latest_article =Blog.objects.filter(latest_articles=True)
    context = {'blogs':blogs,
                'featured_story':featured_story,
                'latest_new':latest_new,
                'latest_article':latest_article,
                

                }

    return render(request, 'cms/admin-blog/posts/index.html', context)

def createBlog(request):
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminblog')
    context = {'form':form}
    return render(request, 'cms/admin-blog/posts/create.html', context)

def updateBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('adminblog')
    context = {'form':form}
    return render(request, 'cms/admin-blog/posts/create.html', context)

def deleteBlog(request, pk):
    deleteblog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        deleteblog.delete()
        return redirect('adminblog')
    context = {'deleteblog': deleteblog}
    return render(request, 'cms/admin-blog/posts/delete.html', context)

#normal pages for users views
def home(request):
    #projects = Project.objects.all()
    #context = {'projects':projects}
    return render(request, 'cms/index.html')


def about(request):
    return render(request, 'cms/about.html')


def contact(request):
    return render(request, 'cms/contact.html')


def register(request):
    return render(request, 'cms/register.html')


def login(request):
    return render(request, 'cms/login.html')


def courses(request):
    courses_field = Course.objects.all()
    context = {'courses_field':courses_field}
    return render(request, 'cms/course.html', context)


def trade_history(request):
    cmss = Cms.objects.all()
    context = {'cmss':cmss}
    return render(request, 'cms/trade.html',context)


def onlinestore(request):
    store_field = Store.objects.all()
    context = {'store_field':store_field}
    return render(request, 'cms/store.html', context)


def blog(request):
    blogs = Blog.objects.all()
    featured_story =Blog.objects.filter(featured_stories=True)
    latest_new =Blog.objects.filter(latest_news=True)
    latest_article =Blog.objects.filter(latest_articles=True)
    context = {'blogs':blogs,
                'featured_story':featured_story,
                'latest_new':latest_new,
                'latest_article':latest_article,
                

                }

    return render(request, 'cms/blog.html', context)

#def singleBlog(request, pk):
    #blogobj = Blog.objects.get(id=pk)
    #print('blogobj:', blogobj)
    #return render(request, 'cms/single.html', {'single-blog': blogobj})

def faqs(request):
    return render(request, 'cms/faqs.html')

def Auth(request):
    return render(request, 'cms/auth.html')

