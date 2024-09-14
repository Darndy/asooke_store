#!/usr/bin/env python
"""Django's command-line utility for admins tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    
    # Set the default Django settings module for the 'store' project.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    
    try:
        # Import the function that executes commands from the command line.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise an error if Django is not installed or if there's an issue with the environment setup.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command-line arguments passed to the script.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Call the main function if this script is run directly (not imported).
    main()
