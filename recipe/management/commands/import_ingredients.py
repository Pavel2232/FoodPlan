import os.path
from random import randint

from django.conf import settings
from django.core.management.base import BaseCommand

from recipe.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        ingredients_file_path = os.path.join(
            settings.BASE_DIR, 'data', 'ingredients.txt'
        )
        with open(ingredients_file_path, 'r') as file:
            ingredients = [line.split(',')[0] for line in file.readlines()]
        bulk = [
            Ingredient(name=ingredient, calories=randint(200, 500))
            for ingredient in ingredients
        ]
        Ingredient.objects.bulk_create(bulk)
