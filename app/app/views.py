from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.create_user(username=username,password = password, email = email)
        user.save
        print('user created')
        return redirect('/')

    return render(request, 'signup.html', {"form": form})

def sign_in(request):
        email = request.POST.get('email')
        password= request.POST.get('password')
        print(email,password)
        return render(request,'login.html')
    