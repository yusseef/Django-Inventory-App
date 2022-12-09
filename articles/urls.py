from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView, name='HomeView'),
    path('article/', ArticleSearchView, name='ArticleSearchView'),
    path('<str:id>/', ArticleView, name='ArticleView'),
]