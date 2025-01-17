"""
WSGI config for stream project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stream.settings')

application = get_wsgi_application()

# gunicorn stream.wsgi:application --bind 0.0.0.0:8000 --limit-request-field_size 16384
