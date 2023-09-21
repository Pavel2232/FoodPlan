from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=50)
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


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    calories = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name}'


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    measurement_unit = models.ForeignKey(
        MeasurementUnit, on_delete=models.CASCADE
    )
