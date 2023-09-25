from django.urls import path

from recipe.views import simple_recipe_view, successfully_subscription, order_view, contacts_view

urlpatterns = [
    path('simple-recipe/', simple_recipe_view, name='simple-recipe'),
    path('successfully_subscription', successfully_subscription, name='successfully_subscription'),
    path('order/', order_view, name='order'),
    path('contacts/', contacts_view, name='contacts'),
]
