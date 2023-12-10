from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email
from .models import User
from django.contrib.auth import logout


def about(request):
    return render(request, 'index.html')
    
def sign_up(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')
        password2 = request.POST.get('password2') 
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, f"Your email is not correct!")
        if password!=password2:
            messages.error(request, f"Your passwords are different! Check your password")
        try: 
            new_user = User.objects.create(username=username,email=email,password=password)
        except ObjectDoesNotExist as d:
            messages.error(request, f"Email is already in use")
        new_user.save()
        print(new_user.email)
        messages.success(request, f"You registered! Thank you!")

    return render(request, 'signup.html')

def sign_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password= request.POST.get('password')
        username = User.objects.get(email=email).username
        user = authenticate(username=username, password=password)
        print('aaaaaaaaaaaaa',user)
        if user is not None:
            login(request, user)
            messages.success(request, f"You loged in! Thank you!")
            print('Loged')
        else: 
            messages.success(request, f"Not loged")
    return render(request,'login.html')
    
def logout(request):
    logout(request)
    return redirect('/about')
    