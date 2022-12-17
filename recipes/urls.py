from django.urls import path
from .views import *
app_name = 'recipes'
urlpatterns = [
    path('list/', recipe_list, name = 'recipelist'),
    path('create/', recipe_create, name = 'recipecreate'),
    path('<str:id>/update/', recipe_update, name = 'recipeupdate'),
    path('<str:id>/', recipe_detail, name = 'recipedetail'),

]