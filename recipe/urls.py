from django.urls import path

from recipe.views import simple_recipe_view, detail_recipe_view, order_view, contacts_view

urlpatterns = [
    path('simple-recipe/', simple_recipe_view, name='simple-recipe'),
    path('detail-recipe/', detail_recipe_view, name='detail-recipe'),
    path('order/', order_view, name='order'),
    path('contacts/', contacts_view, name='contacts'),
]
