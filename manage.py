#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.commands.runserver import Command as Runserver
import time
from selenium import webdriver

channel_access_token=''

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GooderMessage.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    os.system("cd LINE_Bot_Product/GooderMessage && python manage.py runserver")

#

if __name__ == '__main__':
    Runserver.default_addr = '127.0.0.1'
    Runserver.default_port = '3000'
    main()
    


