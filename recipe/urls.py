from django.urls import path

from recipe.views import simple_recipe_view, successfully_subscription, order_view, contacts_view, blog_view, recipe_detail, my_blog

urlpatterns = [
    path('simple-recipe/', simple_recipe_view, name='simple-recipe'),
    path('successfully_subscription', successfully_subscription, name='successfully_subscription'),
    path('order/', order_view, name='order'),
    path('contacts/', contacts_view, name='contacts'),
    path('blog/', blog_view, name='blog'),
    path('my_blog/', my_blog, name='my_blog'),
    path('card1/<int:recipe_id>/', recipe_detail, name='card1'),
]
