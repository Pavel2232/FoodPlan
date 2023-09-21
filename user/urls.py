from django.urls import path
from user.views import registration_view, auth_view, personal_account_view, login, registration
app_name = 'user'
urlpatterns = [
    path('auth/', login, name='login'),
    path('lk/', personal_account_view, name='lk'),
    path('registration/', registration, name='registration'),
]
