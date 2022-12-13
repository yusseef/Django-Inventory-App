from django.contrib import admin
from .models import *

admin.site.register(Recipes)
admin.site.register(RecipeIngredient)

# Register your models here.
