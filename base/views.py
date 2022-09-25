from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def registerUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request , "Registered Successfully")
            return redirect('home')
        messages.error(request, "There was an error during registration")
    form = NewUserForm()
    context = {"form" : form}
    return render (request, 'base/register.html', context)

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in.")
                return redirect("home")
            else:
                messages.error(request, "Username or Password is Incorrect.")
        else:
            messages.error(request, "Username or Password is Incorrect.")
    form = AuthenticationForm()
    context = {"form" : form}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return redirect('home')