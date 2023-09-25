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
    name = models.CharField(max_length=60, verbose_name='Название')
    diet = models.IntegerField(choices=DIET_CHOICES, verbose_name='Меню')
    ingredients = models.ManyToManyField(
        'recipe.Ingredient', through='recipe.RecipeIngredient', verbose_name='Состав'
    )
    fish = models.BooleanField(default=False, verbose_name='Рыба')
    meat = models.BooleanField(default=False, verbose_name='Мясо')
    wheat = models.BooleanField(default=False, verbose_name='Зерновые')
    honey = models.BooleanField(default=False, verbose_name='Продукты пчеловодства')
    nuts = models.BooleanField(default=False, verbose_name='Орехи')
    dairy = models.BooleanField(default=False, verbose_name='Молочные продукты')
    meal = models.IntegerField(choices=MEAL_CHOICES, verbose_name='Приём пищи')
    image = models.ImageField(blank=True, verbose_name='Фото рецепта')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def total_calories(self):
        total_calories = 0
        for recipe_ingredient in self.recipeingredient_set.all():
            total_calories += recipe_ingredient.ingredient.calories / 100 * recipe_ingredient.amount
        return int(total_calories)



    def __str__(self):
        return '{} {}'.format(self.name, self.diet)


class Ingredient(models.Model):
    MEASUREMENT = [
        (1, 'Шт'),
        (2, 'Гр.'),
        (3, 'Мл'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    calories = models.PositiveIntegerField(verbose_name='Калории')
    measurement = models.IntegerField(choices=MEASUREMENT, default=2)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент')
    amount = models.PositiveIntegerField(verbose_name='Вес')

    class Meta:
        verbose_name = 'Рецепт-ингредиент'
        verbose_name_plural = 'Рецепт-ингредиенты'


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец подписки', related_name='subscription')
    diet = models.IntegerField(choices=DIET_CHOICES, verbose_name='Меню')
    people_number = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Value must be at least 1."),
            MaxValueValidator(6, message="Value cannot be greater than 6.")
        ], verbose_name='На сколько персон'
    )
    fish = models.BooleanField(default=False, verbose_name='Рыба')
    meat = models.BooleanField(default=False, verbose_name='Мясо')
    wheat = models.BooleanField(default=False, verbose_name='Зерновые')
    honey = models.BooleanField(default=False, verbose_name='Продукты пчеловодства')
    nuts = models.BooleanField(default=False, verbose_name='Орехи')
    dairy = models.BooleanField(default=False, verbose_name='Молочные продукты')
    TERM_CHOICES = [
        (1, '1 мес.'),
        (2, '3 мес.'),
        (3, '6 мес.'),
        (4, '12 мес.'),
    ]
    term = models.IntegerField(choices=TERM_CHOICES, verbose_name='Срок подписки')
    breakfast = models.BooleanField(default=True, verbose_name='Завтрак')
    lunch = models.BooleanField(default=True, verbose_name='Обед')
    dinner = models.BooleanField(default=True, verbose_name='Ужин')
    dessert = models.BooleanField(default=True, verbose_name='Десерт')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def total_meal(self):
        meal = 0
        if self.lunch:
            meal += 1
        if self.breakfast:
            meal += 1
        if self.dinner:
            meal += 1
        if self.dessert:
            meal += 1
        return meal

    def description_menu(self):
        if self.diet == 1:
            return 'Норм хавчик'
        if self.diet == 2:
            return 'Типо схудну'
        if self.diet == 3:
            return 'Мясо отстой'
        if self.diet == 4:
            return 'Много жира, мало протеина'

    def none_allergy(self):
        if True not in [self.honey, self.fish, self.nuts, self.wheat, self.meat, self.dairy]:
            return None
