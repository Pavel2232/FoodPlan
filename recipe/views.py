from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def order_view(request):
    return render(request, 'order.html')


def simple_recipe_view(request):
    return render(request, 'card1.html')


def detail_recipe_view(request):
    return render(request, 'card2.html')

def contacts_view(request):
    return render(request, 'contacts.html')
