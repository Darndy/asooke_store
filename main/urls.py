from .views import *
from django.urls import path


urlpatterns = [
    path('', index),
    path('login/', loginview),
    path('register/', register),
    path('logout/', logoutview),
    path('dashboard/', market),
]