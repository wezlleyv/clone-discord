from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from .forms import *

from .models import User

# Create your views here.
def loginasview(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('app')
        else:
            return redirect("login")
    else:
        context = {}
        context['form'] = Login()
        return render(request, "login.html", context)

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.cleaned_data['email'], name=form.cleaned_data['name'], password=form.cleaned_data['password']) 
            user.save()  
            return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': Register})

def logoutasview(request):
    logout(request)
    return redirect('login')