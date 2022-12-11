from django.urls import path
from .views import *
urlpatterns = [
    path('login/', AccountLoginView, name='AccountLogin'),
    path('logout/', AccountLogoutView, name='AccountLogout'),
    path('register/', AccountRegisterView, name='AccountRegister'),
]