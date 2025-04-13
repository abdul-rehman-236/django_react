# settings/prod.py
from .base import *

# Production Specific Settings
DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='your_production_domain', cast=Csv())

# Database Configuration for Production (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT', default='5432'),
    }
}

# Security Settings for Production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # Ensure all traffic is HTTPS
X_FRAME_OPTIONS = 'DENY'

# Static files (for production)
STATIC_ROOT = BASE_DIR / 'staticfiles'
