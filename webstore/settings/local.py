from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'rest_framework', 'django_filters')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
}
