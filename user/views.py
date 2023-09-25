from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from recipe.models import Subscription, RecipeIngredient, Recipe
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
    subscription = Subscription.objects.get(user_id=request.user.id)
    meal_c = 0
    if subscription.breakfast:
        meal_c += 1
    if subscription.dinner:
        meal_c += 1
    if subscription.lunch:
        meal_c += 1
    if subscription.dessert:
        meal_c += 1
    recipes = Recipe.objects.filter(diet=subscription.diet)
    context = {'title': 'Личный кабинет', 'form': form, 'subscription': subscription,  'recipes': recipes}
    return render(request, 'lk.html', context, )
