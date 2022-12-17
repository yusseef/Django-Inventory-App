from django.db import models
from django.conf import settings
from .validators import validate_unit
from .utils import number_str_to_float
from django.urls import reverse

User = settings.AUTH_USER_MODEL
# Create your models here.



class Recipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:recipedetail", kwargs= {"id":self.id})
       
        

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank = True, null=True)
    unit = models.CharField(max_length=500, validators=[validate_unit] )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def get_absolute_url(self):
        return recipe.get_absolute_url()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_float, qty_floatsuccess = number_str_to_float(qty)
        if qty_floatsuccess:
            self.quantity_as_float = qty_float 
        
        else:
            self.quantity_as_float = None
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name