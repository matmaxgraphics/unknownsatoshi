from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)


            return redirect('blog')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

 
    
def logout(request):
    logout(request)
    return redirect('home')