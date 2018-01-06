# -*- coding: utf-8 -*-

from os import environ, path

from pgconninfo import pg_conninfo


# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))


# Security

SECRET_KEY = environ.get('DJANGO_SECRET_KEY')
DEBUG = len(environ.get('DJANGO_DEBUG', '')) > 0
ALLOWED_HOSTS = environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

# CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database

DATABASES = {
    'default': pg_conninfo(),
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGES_AVAILABLE = {
    'en': u'English',
    'ar': u'العربية',
}
LANGUAGES = [
    (x, LANGUAGES_AVAILABLE[x]) \
    for x in os.environ.get('DJANGO_LANGUAGES', '').split(',') \
    if x in LANGUAGES_AVAILABLE
]
LANGUAGES = [
    (x, LANGUAGES_AVAILABLE[x]) for x in LANGUAGES_AVAILABLE
] if (len(LANGUAGES) == 0)
LANGUAGE_CODE = LANGUAGES[0][0]

TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_L10N = True
DATE_INPUT_FORMATS = ['%Y-%m-%d', '%d/%m/%Y']
USE_TZ = True

# Static files (CSS, JavaScript, Images)

MEDIA_URL = '/media/'
MEDIA_ROOT = environ.get('DJANGO_MEDIA_ROOT', path.join(BASE_DIR, 'media'))

STATIC_URL = '/static/'
STATIC_ROOT = environ.get('DJANGO_STATIC_ROOT', None)
STATICFILES_DIRS = [path.join(BASE_DIR, 'static'),]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

EMAIL_HOST = environ.get('DJANGO_EMAIL_HOST')
EMAIL_PORT = environ.get('DJANGO_EMAIL_PORT')
EMAIL_HOST_USER = environ.get('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = environ.get('DJANGO_EMAIL_USE_TLS')
EMAIL_USE_SSL = environ.get('DJANGO_EMAIL_USE_SSL')

# Uploads

MAX_ITEM_IMAGES = environ.get('DJANGO_MAX_ITEM_IMAGES', 5)
FILE_UPLOAD_MAX_SIZE = environ.get('DJANGO_FILE_UPLOAD_MAX_SIZE', 10)  # MB
DATA_UPLOAD_MAX_MEMORY_SIZE = None

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'syslog': {
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(message)s'
        },
    },
    'handlers': {
        'syslog': {
            'class': 'logging.handlers.SysLogHandler',
            'facility': environ.get('DJANGO_LOG_FACILITY', 'local7'),
            'formatter': 'syslog',
        },
    },
    'loggers': {
        '': {
            'level': environ.get('DJANGO_LOG_LEVEL', 'DEBUG' if DEBUG else 'INFO'),
            'handlers': ['syslog'],
            'propagate': True,
        },
    },
}
