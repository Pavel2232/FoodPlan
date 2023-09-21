from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient


class RecipeIngredientItemInline(admin.TabularInline):
    model = RecipeIngredient
    raw_id_fields = ['ingredient']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientItemInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
