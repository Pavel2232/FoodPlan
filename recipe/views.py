from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from recipe.models import Subscription
from user.models import CustomUser


# Create your views here.
def index_view(request):
    if request.user.id is None:
        return render(request, 'index.html')
    else:
        return render(request, 'index_sign.html')


def order_view(request):
    if request.user.is_active:
        return render(request, 'order.html')
    else:
        return redirect(reverse('user:login'))


def simple_recipe_view(request):
    return render(request, 'card1.html')


def successfully_subscription(request):
    allergy1 = False
    allergy2 = False
    allergy3 = False
    allergy4 = False
    allergy5 = False
    allergy6 = False
    select1 = False
    select2 = False
    select3 = False
    select4 = False
    print( request.GET)
    if int(request.GET.get('select1')) == 0:
        select1 = True
    if int(request.GET.get('select2')) == 0:
        select2 = True
    if int(request.GET.get('select3')) == 0:
        select3 = True
    if int(request.GET.get('select4')) == 0:
        select4 = True

    if request.GET.get('allergy1'):
        allergy1 = True
    if request.GET.get('allergy2'):
        allergy2 = True
    if request.GET.get('allergy3'):
        allergy3 = True
    if request.GET.get('allergy4'):
        allergy4 = True
    if request.GET.get('allergy5'):
        allergy5 = True
    if request.GET.get('allergy6'):
        allergy6 = True
    Subscription.objects.create(
        user=CustomUser.objects.get(id=request.user.id),
        diet=int(request.GET.get('foodtype')),
        people_number=int(request.GET.get('select5')),
        fish=allergy1,
        meat=allergy2,
        wheat=allergy3,
        honey=allergy4,
        nuts=allergy5,
        dairy=allergy6,
        term=int(request.GET.get('sub')),
        breakfast=select1,
        lunch=select2,
        dinner=select3,
        dessert=select4,
    )

    return render(request, 'successfully_subscription.html')


def contacts_view(request):
    return render(request, 'contacts.html')
