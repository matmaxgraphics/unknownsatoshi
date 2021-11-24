from django.urls import path
from django.contrib.auth import  views as aut_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name="logout"),
    path('login/', aut_views.LoginView.as_view(template_name='login.html'), name='login'),
    
]
 