from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')  # шаблон home.html

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'base.html')  # твой шаблон для регистрации

def logout_view(request):
    return redirect('home')
