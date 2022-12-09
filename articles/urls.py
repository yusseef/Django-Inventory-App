from django.urls import path
from .views import *
urlpatterns = [
    path('', ArticListView, name='ArticListView'),
    path('article/', ArticleSearchView, name='ArticleSearchView'),
    path('article/create/', ArticleCreateView, name='ArticleCreateView'),
    path('<str:id>/', ArticleView, name='ArticleView'),
]