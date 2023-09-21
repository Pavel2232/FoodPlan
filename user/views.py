from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from user.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:lk'))
    else:
         form = UserLoginForm()
    context = {'form': form}
    return render(request, 'auth.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'registration.html', context)


def auth_view(request):
    return render(request, 'auth.html')


def personal_account_view(request):
    return render(request, 'lk.html')


def registration_view(request):
    return render(request, 'registration.html')
