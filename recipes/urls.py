from django.urls import path
from .views import *
urlpatterns = [
    path('list/', index, name = 'index'),
]