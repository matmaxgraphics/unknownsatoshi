from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # main website views
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('faqs/', views.faqs, name='faqs'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('trade-history/', views.trade_history, name='trade-history'),
    path('onlinestore/', views.onlinestore, name='onlinestore'),
    path("subscription/", views.premium_subscription, name="premium-subscription"),
    path('notauth/', views.Auth, name='notauth'),
    
    # admin panel
    path('adminpanel', views.adminpanel, name='adminpanel'),
    
    # admin login panel
    path('adminlogin', auth_views.LoginView.as_view(template_name='cms/admin-login.html'), name='adminlogin'),
    
    # admin logout
    path('logout/', views.logoutadmin, name="logout"),
    
    # admin history section
    path('adminhistory', views.adminhistory, name='adminhistory'),
   
    # admin product section
    path('admin-product', views.admin_product, name='admin-product'),
    path('create-product/', views.create_product, name='create-product'),
    path('update-product/<str:pk>/', views.update_product, name='update-product'),
    path('delete-product/<str:pk>/', views.delete_product, name='delete-product'),

    # admin trade section
    path('create-trade/', views.createTrade, name='create-trade'),
    path('trade/<str:pk>/', views.trade, name='trade'),
    path('delete-trade/<str:pk>/', views.deleteTrade, name='delete-trade'),
    path('update-trade/<str:pk>/', views.updateTrade, name='update-trade'),

    # admin course section
    path('admincourse', views.admincourse, name='admincourse'),
    path('create-course/', views.createCourse, name='create-course'),
    path('update-course/<str:pk>/', views.updateCourse, name='update-course'),
    path('delete-course/<str:pk>/', views.deleteCourse, name='delete-course'),

    
    
    # admin blog section
    path('create-blog/', views.create_blog, name='create-blog'),
    path('adminblog/', views.admin_blog, name='adminblog'),
    path('update-blog/<str:pk>/', views.update_blog, name='update-blog'),
    path('delete-blog/<str:pk>/', views.delete_blog, name='delete-blog'),
    path('blog-detail/<str:pk>/', views.blog_detail, name='blog-detail'),
]