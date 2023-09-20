from django.urls import path
from user.views import registration_view, auth_view, personal_account_view

urlpatterns = [
    path('auth/', auth_view, name='login'),
    path('lk/', personal_account_view, name='lk'),
    path('registration/', registration_view, name='registration'),
]
