from django.apps import AppConfig  # Import Django's AppConfig class to configure application settings


# Define the configuration class for the 'main' app
class MainConfig(AppConfig):
    # Specifies the default field type for auto-generated primary keys (BigAutoField for large integer values)
    default_auto_field = 'django.db.models.BigAutoField'

    # Defines the name of the application, which corresponds to the app's folder name ('main')
    name = 'main'
