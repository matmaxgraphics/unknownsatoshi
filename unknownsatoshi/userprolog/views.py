from django.conf import settings
import urllib3, urllib, json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from cms.mailing_helper import UserSubscriptionNotification
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from userprolog.models import User
from django.contrib import messages
from cms.models import SubscriptionHistory
from .token import account_activation_token
from .decorators import unauthenticated_user
from unknownsatoshi.settings import DEFAULT_FROM_EMAIL

from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode




# user registeration
@unauthenticated_user
def user_register(request):
    template_name = 'userprolog/register.html'
    if request.method =="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_no = request.POST.get("phone_no")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        #captcha config
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode('utf-8')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        result = json.load(response)
        # end of captcha config
            
        if User.objects.filter(username=username).exists():
            messages.error(request, f"username already exists")
            return redirect("register")

        elif User.objects.filter(email=email).exists():
            messages.error(request, f"email already exits")
            return redirect("register")

        elif password1 != password2:
            messages.error(request, f"password do not match")
            return redirect("register")

        elif not result["success"]:
            messages.error(request, f"Invalid reCAPTCHA. Please try again.")
            return redirect("register")
        
        else:
            user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, phone_no=phone_no,is_active=False, is_staff=False, is_superuser=False)
            user.set_password(password1)
            user.save()
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
    
            # set up email activation
            current_site = get_current_site(request)
            subject = "Activate your Account"
            html_message = render_to_string('userprolog/activate_account.html',{
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            message = strip_tags(html_message)
            send_mail = UserSubscriptionNotification(email_subject=subject, email_body=message, sender_email=DEFAULT_FROM_EMAIL, receiver_email=user.email)
            send_mail.mail_user()
            return render(request, "userprolog/activation_link_sent.html")
    else:
        return render(request, template_name)


#activate account       
def account_activation(request, uidb64, token):
    admin_user = User.objects.filter(is_superuser=True)
    subject = "Account Activation Status"
    message = "Your account has been successfully activate, you can proceed to login if you are already not logged in"
    uid = None
    user = None
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except:
        pass
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        for ad_user in admin_user:
            send_mail = UserSubscriptionNotification(email_subject=subject, email_body=message, sender_email=DEFAULT_FROM_EMAIL, receiver_email=ad_user.email)
        send_mail.mail_user
        #send_mail.mail_admin
        return redirect("activation-success")
    else:
        template_name = "userprolog/activation_invalid.html"
        return render(request, template_name)


def activation_success(request):
    template_name = "userprolog/activation_success.html"
    return render(request, template_name)


# user login
@unauthenticated_user
def user_login(request):
    template_name = 'userprolog/login.html'
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_active == False:
                messages.error(request, f"Your account is pending activation")
                return redirect("user-login")

            if "next" in request.POST:
                return redirect(request.POST.get("next"))

            messages.success(request, f"login successful")
            return redirect("home")
        messages.error(request, f"login attempt failed, try again")
        return redirect("user-login")
    return render(request, template_name)


#user log out
def logout_user(request):
    logout(request)
    messages.success(request, f"logout successful")
    return redirect('home')


#user profile and update 
@login_required(login_url="user-login")   
def user_profile(request, id):
    template_name = "userprolog/profile.html"
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            update_form = form.save(commit=False)
            update_form.is_active = True
            update_form.save()
            messages.success(request, f"User updated successfully")
            return redirect("user-profile", id)
        messages.error(request, f"Unable to update user")
        return redirect("user-profile", id)
    else:
        form = UserUpdateForm(instance=user)
    context = {"form":form, "user":user}
    return render(request, template_name, context)


@login_required(login_url='user-login')
def user_subscription_list(request):
    user = request.user
    subscription = SubscriptionHistory.objects.filter(user=user)
    template_name = "userprolog/sub-plan.html"
    context = {"subscription":subscription,"user":user}
    return render(request, template_name, context)