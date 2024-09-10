from .views import *
from django.urls import path


urlpatterns = [
    path('', landing),
    path('login/', loginview),
    path('register/', register),
    path('logout/', logoutview),
    path('dashboard/', index),
]