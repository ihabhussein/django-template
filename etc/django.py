# -*- coding: utf-8 -*-

from project.settings import *

from pgconninfo import pg_conninfo


# Security

SECRET_KEY = 'uxM7z/bzeFWp9cqRb8MS8Znkg97PbcJLvXSJ535bFB4uR1sb+OWSX'
DEBUG = 0
ALLOWED_HOSTS = ['*']

# CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True


# Database

DATABASES = {
    'default': pg_conninfo(),
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }
}


# Internationalization

LANGUAGES = [
    ('en', u'English'),
    ('ar', u'العربية'),
]
LANGUAGE_CODE = 'en'


EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = environ.get('EMAIL_USE_TLS')
EMAIL_USE_SSL = environ.get('EMAIL_USE_SSL')
