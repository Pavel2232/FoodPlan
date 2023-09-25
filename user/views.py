from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from recipe.models import Subscription
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages


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
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы')
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:lk'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    subscription = Subscription.objects.filter(user_id=request.user.id)
    meal_c = 0
    for meal in subscription[:1]:
        if meal.breakfast:
            meal_c += 1
        if meal.dinner:
            meal_c += 1
        if meal.lunch:
            meal_c += 1
        if meal.dessert:
            meal_c += 1
    callories = 0
    # for callorie in subscription[:1]:
    #     callorie.
    context = {'title': 'Личный кабинет', 'form': form, 'subscription': subscription[:1], 'meal': meal_c}
    return render(request, 'lk.html', context, )
