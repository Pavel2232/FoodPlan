# Generated by Django 4.2.5 on 2023-09-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.IntegerField(choices=[(1, 'Classic'), (2, 'Low carb'), (3, 'Vegan'), (4, 'Keto')])),
            ],
        ),
    ]
