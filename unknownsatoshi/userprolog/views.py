from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from userprolog.models import User
from django.contrib import messages
from .forms import *
from .decorators import unauthenticated_user



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
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "username already exists")
            return redirect("register")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "email already exits")
            return redirect("register")

        elif password1 != password2:
            messages.error(request, "password do not match")
            return redirect("register")
        else:
            user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, phone_no=phone_no,is_active=True, is_staff=False, is_superuser=False)
            user.set_password(password1)
            user.save()
            group = Group.objects.get(id=2)
            user.groups.add(group)
            login(request,user)
            messages.success(request, "Account successfuly created")
            return redirect("user-login")
    else:
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
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            messages.success(request, f"login successful")
            return redirect("home")
        messages.error(request, f"login attempt failed")
        return redirect("user-login")
    return render(request, template_name)


#user log out
def user_logout(request):
    logout(request)
    messages.success(request, f"logout successful")
    return redirect('home')


#user profile and update     
def user_profile(request, id):
    template_name = "userprolog/profile.html"
    user = get_object_or_404(User, id=id)
    form = UserUpdateForm()
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.is_active = True
            form.save()
            messages.success(request, f"User updated successfully")
            return redirect("user-profile", id)
        messages.error(request, f"Unable to update user")
        return redirect("user-profile", id)
    else:
        form = UserUpdateForm(instance=user)
    context = {"form":form, "user":user}
    return render(request, template_name, context)