from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient, Subscription


class RecipeIngredientItemInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientItemInline]
    list_display = ['name', 'diet']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
