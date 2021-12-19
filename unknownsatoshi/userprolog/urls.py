from django.urls import path
from django.contrib.auth import  views as auth_views
from .views import *

urlpatterns = [
    path('user-registration', user_register, name='register'),
    path('account/activate/<str:uidb64>/<str:token>', account_activation, name="account-activation"),
    path("activation-success", activation_success, name="activation-success"),
    path('login/user', user_login, name='user-login'),
    path('logout', user_logout, name="user-logout"),
    path('user/profile/<str:id>', user_profile, name="user-profile"),
    path('subscription/history/', user_subscription_list, name="user-sub-list"),

    #password reset
    path('reset-password/', 
        auth_views.PasswordResetView.as_view(template_name = "userprolog/reset_password.html"), 
        name ='reset_password'),
    
    path('reset-password-sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name = "userprolog/password_reset_sent.html"), 
        name ='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = "userprolog/password_reset_change.html"), 
        name ='password_reset_confirm'),
    
    path('reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = "userprolog/password_reset_done.html"), 
        name ='password_reset_complete'),
]

 