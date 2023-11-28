from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', { 'form': form})
def sign_in(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'login.html', { 'form': form})