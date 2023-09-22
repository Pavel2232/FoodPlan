from django.db import models

from user.models import CustomUser


class Recipe(models.Model):
    name = models.CharField(max_length=60)
    DIET_CHOICES = [
        (1, 'Classic'),
        (2, 'Low carb'),
        (3, 'Vegan'),
        (4, 'Keto'),
    ]
    diet = models.IntegerField(choices=DIET_CHOICES)
    ingredients = models.ManyToManyField(
        'recipe.Ingredient', through='recipe.RecipeIngredient'
    )
    fish = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    wheat = models.BooleanField(default=False)
    honey = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    dairy = models.BooleanField(default=False)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    DIET_CHOICES = [
        (1, 'Classic'),
        (2, 'Low carb'),
        (3, 'Vegan'),
        (4, 'Keto'),
    ]
    diet = models.IntegerField(choices=DIET_CHOICES)
