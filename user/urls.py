from django.urls import path
from user.views import login, registration, profile
app_name = 'user'
urlpatterns = [
    path('auth/', login, name='login'),
    path('lk/', profile, name='lk'),
    path('registration/', registration, name='registration'),
]
