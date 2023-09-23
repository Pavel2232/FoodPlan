from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from user.models import CustomUser


MEAL_CHOICES = [
        (1, 'Завтраки'),
        (2, 'Обеды'),
        (3, 'Ужины'),
        (4, 'Десерты'),
    ]

DIET_CHOICES = [
        (1, 'Classic'),
        (2, 'Low carb'),
        (3, 'Vegan'),
        (4, 'Keto'),
    ]


class Recipe(models.Model):
    name = models.CharField(max_length=60)
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
    meal = models.IntegerField(choices=MEAL_CHOICES)


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
    diet = models.IntegerField(choices=DIET_CHOICES)
    people_number = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Value must be at least 1."),
            MaxValueValidator(6, message="Value cannot be greater than 6.")
        ]
    )
    fish = models.BooleanField(default=False)
    meat = models.BooleanField(default=False)
    wheat = models.BooleanField(default=False)
    honey = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    dairy = models.BooleanField(default=False)
    TERM_CHOICES = [
        (1, '1 мес.'),
        (2, '3 мес.'),
        (3, '6 мес.'),
        (4, '12 мес.'),
    ]
    term = models.IntegerField(choices=TERM_CHOICES)
    meal = models.IntegerField(choices=MEAL_CHOICES)
