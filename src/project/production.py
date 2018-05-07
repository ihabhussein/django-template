# -*- coding: utf-8 -*-

from os import environ
from pgconninfo import pg_conninfo
from project.settings import *


# Security

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')
DEBUG = False
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


# Internationalization

LANGUAGES = [
    ('en', u'English'),
    ('ar', u'العربية'),
]
LANGUAGE_CODE = 'en'


# Mail

EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT = environ.get('EMAIL_PORT')
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = environ.get('EMAIL_USE_TLS')
EMAIL_USE_SSL = environ.get('EMAIL_USE_SSL')
