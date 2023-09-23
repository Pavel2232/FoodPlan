from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import path, include
from django.views import defaults as default_views
from recipe.views import index_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index_view, name='home'),
    path('recipe/', include('recipe.urls')),
    path('user/', include('user.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += (
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("У вас нет доступа.")}),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Страница не найдена.")}),
        path("500/", default_views.server_error),
    )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)