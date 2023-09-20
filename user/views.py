from django.shortcuts import render


# Create your views here.
def auth_view(request):
    return render(request, 'auth.html')


def personal_account_view(request):
    return render(request, 'lk.html')


def registration_view(request):
    return render(request, 'registration.html')
