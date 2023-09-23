from django.shortcuts import render


# Create your views here.
def index_view(request):
    if request.user.id is None:
        return render(request, 'index.html')
    else:
        return render(request, 'index_sign.html')

def order_view(request):
    return render(request, 'order.html')


def simple_recipe_view(request):
    return render(request, 'card1.html')


def detail_recipe_view(request):
    return render(request, 'card2.html')
