# Generated by Django 4.2.5 on 2023-09-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_ingredient_rename_genre_recipe_diet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='dairy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='fish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='honey',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='nuts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='wheat',
            field=models.BooleanField(default=False),
        ),
    ]