from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def signup_page(request):
    context = {}
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            context['error'] = 'The given username already exists! Please enter a different username.'
            return render(request, 'auth_system/signup.html', context)
        except User.DoesNotExist:
            if request.POST['password-1'] != request.POST['password-2']:
                context['error'] = 'The passwords you entered are not the same! Please enter same passwords.'
                return render(request, 'auth_system/signup.html', context)
            else:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                                password=request.POST['password-1'])
                auth.login(request, user)
                return redirect('home')
    else:
        return render(request, 'auth_system/signup.html', context)


def login_page(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            if request.POST.get('redir'):
                return redirect(f'{request.POST.get("redir")}')
            else:
                return redirect('home')
        else:
            context['error'] = 'The entered password or login is incorrect! Please enter correct data.'
            return render(request, 'auth_system/login.html', context)
    else:
        if request.GET.get('next'):
            context['next'] = 'Only logged in users can access this page! Log in.'
            context['nextURL'] = request.GET.get('next')
        return render(request, 'auth_system/login.html')

@login_required
def logout_page(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def public_page(request):
    return render(request, 'auth_system/publicpage.html')

@login_required
def private_page(request):
    return render(request, 'auth_system/privatepage.html')


class PrivateClass_page(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'auth_system/privateclasspage.html')
