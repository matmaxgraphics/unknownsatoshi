from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('adminlogin', auth_views.LoginView.as_view(template_name='cms/admin-login.html'), name='adminlogin'),
    path('logout/', views.logoutadmin, name="logout"),
    path('adminhistory', views.adminhistory, name='adminhistory'),
    path('admincourse', views.admincourse, name='admincourse'),
    path('adminstore', views.adminStore, name='adminstore'),
    path('create-trade/', views.createTrade, name='create-trade'),
    path('create-course/', views.createCourse, name='create-course'),
    path('create-store/', views.createStore, name='create-store'),
    path('delete-trade/<str:pk>/', views.deleteTrade, name='delete-trade'),
    path('delete-course/<str:pk>/', views.deleteCourse, name='delete-course'),
    path('delete-store/<str:pk>/', views.deleteStore, name='delete-store'),
    path('update-trade/<str:pk>/', views.updateTrade, name='update-trade'),
    path('update-course/<str:pk>/', views.updateCourse, name='update-course'),
    path('update-store/<str:pk>/', views.updateStore, name='update-store'),
    path('update-blog/<str:pk>/', views.updateBlog, name='update-blog'),
    path('trade/<str:pk>/', views.trade, name='trade'),
    path('single-blog/', views.singleBlog, name='single-blog'),
    path('adminblog/', views.adminblog, name='adminblog'),
    path('create-blog/', views.createBlog, name='create-blog'),
    path('delete-blog/<str:pk>/', views.deleteBlog, name='delete-blog'),

    
    
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('trade-history/', views.trade_history, name='trade-history'),
    path('onlinestore/', views.onlinestore, name='onlinestore'),
    path('blog/', views.blog, name='blog'),
    path('faqs/', views.faqs, name='faqs'),
    path('notauth/', views.Auth, name='notauth'),

    #path('project/<str:pk>/', views.project, name='project'),

    #path('create-project/', views.createProject, name='create-project'),
    #path('update-project<str:pk>/', views.updateProject, name='update-project'),
    #path('delete-project<str:pk>/', views.deleteProject, name='delete-project'),
]