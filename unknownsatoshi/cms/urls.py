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
    path("faqs", views.faq_view, name="faq"),
    path("privacy", views.privacy_view, name="privacy"),
    path('trade-history/', views.trade_history, name='trade-history'),
    path('onlinestore/', views.onlinestore, name='onlinestore'),
    path('notauth/', views.Auth, name='notauth'),
    
    # admin panel
    path('admin-dashboard/', views.admin_panel, name='adminpanel'),
    
    # admin login panel
    path('admin-login/', views.admin_login, name='admin-login'),
    
    # admin logout
    path('logout/', views.admin_logout, name="admin-logout"),
    
    # admin history section
    path('admin-history/', views.admin_history, name='admin-history'),
   
    # admin product section
    path('admin-product', views.admin_product, name='admin-product'),
    path('create-product/', views.create_product, name='create-product'),
    path('update-product/<str:id>/', views.update_product, name='update-product'),
    path('delete-product/<str:id>/', views.delete_product, name='delete-product'),

    # admin trade section
    path('create-trade/', views.create_trade, name='create-trade'),
    path('trade/<str:pk>/', views.trade, name='trade'),
    path('delete-trade/<str:pk>/', views.delete_trade, name='delete-trade'),
    path('update-trade/<str:pk>/', views.update_trade, name='update-trade'),

    # admin course section
    path('admincourse', views.admin_course, name='admin-course'),
    path('create-course/', views.create_course, name='create-course'),
    path('update-course/<str:pk>/', views.update_course, name='update-course'),
    path('delete-course/<str:pk>/', views.delete_course, name='delete-course'),

    
    
    # admin blog section
    path('create-blog/', views.create_blog, name='create-blog'),
    path('admin-blog/', views.admin_blog, name='admin-blog'),
    path('update-blog/<str:pk>/', views.update_blog, name='update-blog'),
    path('delete-blog/<str:pk>/', views.delete_blog, name='delete-blog'),
    path('blog-detail/<str:pk>/', views.blog_detail, name='blog-detail'),

    #admin user section.
    path('admin-create-user/', views.admin_create_user, name="admin-create-user"),
    path('admin-user-list/', views.admin_user_list, name="admin-user-list"),
    path('user-update/<str:id>/', views.admin_update_user, name="admin-update-user"),
    path('delete-user/<str:id>/', views.admin_delete_user, name="admin-delete-user"),

    #subscrition section
    path("subscription/plan-list", views.plan_list, name="plan-list"),
    path("subscription/plan-detail/<str:slug>", views.plan_details, name="plan-detail"),
    path('callback', views.payment_response, name='payment_response')
]