from .views import *  # Import all views from the views.py file
from django.urls import path  # Import Django's path function to define URL patterns


# Define the URL patterns for the application
urlpatterns = [
    # Route for the home page, calls the 'index' view
    path('', index),

    # Route for the login page, calls the 'loginview' view
    path('login/', loginview),

    # Route for the registration page, calls the 'register' view
    path('register/', register),

    # Route for the logout function, calls the 'logoutview' view
    path('logout/', logoutview),

    # Route for the dashboard/market page, calls the 'market' view
    path('dashboard/', market),
]
