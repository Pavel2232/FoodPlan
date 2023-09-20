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
