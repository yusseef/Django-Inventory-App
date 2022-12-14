from django.contrib import admin
from .models import *

class RecipeIngredientAdmin(admin.StackedInline):
    model = RecipeIngredient
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientAdmin,]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipes, RecipeAdmin)

# Register your models here.
