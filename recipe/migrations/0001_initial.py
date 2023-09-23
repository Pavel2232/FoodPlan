# Generated by Django 4.2.5 on 2023-09-23 18:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('calories', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('diet', models.IntegerField(choices=[(1, 'Classic'), (2, 'Low carb'), (3, 'Vegan'), (4, 'Keto')])),
                ('fish', models.BooleanField(default=False)),
                ('meat', models.BooleanField(default=False)),
                ('wheat', models.BooleanField(default=False)),
                ('honey', models.BooleanField(default=False)),
                ('nuts', models.BooleanField(default=False)),
                ('dairy', models.BooleanField(default=False)),
                ('meal', models.IntegerField(choices=[(1, 'Завтраки'), (2, 'Обеды'), (3, 'Ужины'), (4, 'Десерты')])),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet', models.IntegerField(choices=[(1, 'Classic'), (2, 'Low carb'), (3, 'Vegan'), (4, 'Keto')])),
                ('people_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Value must be at least 1.'), django.core.validators.MaxValueValidator(6, message='Value cannot be greater than 6.')])),
                ('fish', models.BooleanField(default=False)),
                ('meat', models.BooleanField(default=False)),
                ('wheat', models.BooleanField(default=False)),
                ('honey', models.BooleanField(default=False)),
                ('nuts', models.BooleanField(default=False)),
                ('dairy', models.BooleanField(default=False)),
                ('term', models.IntegerField(choices=[(1, '1 мес.'), (2, '3 мес.'), (3, '6 мес.'), (4, '12 мес.')])),
                ('meal', models.IntegerField(choices=[(1, 'Завтраки'), (2, 'Обеды'), (3, 'Ужины'), (4, 'Десерты')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe.RecipeIngredient', to='recipe.ingredient'),
        ),
    ]