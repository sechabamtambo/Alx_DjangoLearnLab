#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< Updated upstream
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
=======
<<<<<<< HEAD
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
>>>>>>> a3173103943b284f658dae12fad8338bc927ec82
>>>>>>> 3d355f2878a7b71a245317b672e1f7ce0b5f42d5
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
>>>>>>> Stashed changes
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
