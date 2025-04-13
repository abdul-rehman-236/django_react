# settings/dev.py
from .base import *

# Development specific settings
DEBUG = True

# Database Configuration for Development (SQLite for simplicity in development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB', default='django_react_db'),
        'USER': config('POSTGRES_USER', default='django_react_user'),
        'PASSWORD': config('POSTGRES_PASSWORD', default='django_react_password'),
        'HOST': config('POSTGRES_HOST', default='localhost'),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

# Other Development Specific Configurations (optional)
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

