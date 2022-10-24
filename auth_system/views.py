from django.shortcuts import render


def signup_page(request):
    return render(request, 'auth_system/signup.html')


def login_page(request):
    return render(request, 'auth_system/login.html')


def logout_page(request):
    return render(request, 'auth_system/logout.html')
