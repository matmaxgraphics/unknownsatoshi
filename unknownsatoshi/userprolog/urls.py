from django.urls import path
from django.contrib.auth import  views as aut_views
from .views import *

urlpatterns = [
    path('user-registration', user_register, name='register'),
    path('logout', user_logout, name="user-logout"),
    path('user-login', user_login, name='user-login'),
    path('user-profile/<str:id>', user_profile, name="user-profile")
]
 