from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import User


def about(request):
    return render(request, 'index.html')
    
def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        full_n = request.POST.get('full_n')
        email = request.POST.get('email')
        password= request.POST.get('password')
        password2 = request.POST.get('password2') 
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, f"Your email is not correct!")
        if password!=password2:
            messages.error(request, f"Your passwords are different! Check your password")
        new_user = User.objects.create(full_n=full_n,email=email,password=password)
        new_user.save()
        
        #user = User.objects.create_user(username=username,password = password, email = email)
        #user.save

    return render(request, 'signup.html')

def sign_in(request):
        email = request.POST.get('email')
        password= request.POST.get('password')
        print(email,password)
        return render(request,'login.html')
    