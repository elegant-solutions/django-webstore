from .base import *
import os
import datetime

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ('debug_toolbar', 'rest_framework', 'django_filters')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'products.pagination.ProductPagination',
    'SEARCH_PARAM': 'q'
}

JWT_AUTH = {
    "JWT_RESPONSE_PAYLOAD_HANDLER":
                "webstore.utils.jwt_response_payload_handler",
    "JWT_EXPIRATION_DELTA": datetime.timedelta(seconds=30000),
    "JWT_ALLOW_REFRESH": True,
}
