from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from userprolog.models import User
from django.contrib import messages



# user registeration
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
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request, "Account successfuly created")
            return redirect("user-login")
    else:
        return render(request, template_name)
        

# user login
def user_login(request):
    template_name = 'userprolog/login.html'
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"login successful")
            return redirect("home")
        messages.info(request, f"login attempt failed")
        return redirect("user-login")
    return render(request, template_name)


#user log out
def user_logout(request):
    logout(request)
    messages.success(request, f"logout successful")
    return redirect('home')