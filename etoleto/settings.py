# -*- coding: utf-8 -*-
"""
Django settings for etoleto project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.utils.safestring import mark_safe

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_PATH = os.path.realpath(os.path.dirname(__file__))

SUIT_CONFIG = {
    'ADMIN_NAME': mark_safe(u'&laquo;Это Лето&raquo;'),
    'HEADER_DATE_FORMAT': 'l, j E Y',
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@vi^9-trjjd(zr5j_4bf(l2^=tv*)0#6o9vwkg*(w@#fajt^v'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'suit',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party
    'compressor',
    'imagekit',
    'south',
    'flatblocks',

    # site applications
    'base',
    'misc',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.minify.MinifyHTMLMiddleware',
    'base.minify.MarkHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
TEMPLATE_DIRS = (
    os.path.join(CORE_PATH, 'templates'),
)

ROOT_URLCONF = 'etoleto.urls'
WSGI_APPLICATION = 'etoleto.wsgi.application'

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'etoleto',
#         'USER': 'xfenix',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG' if DEBUG else 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

TIME_ZONE = 'Europe/Moscow'
USE_TZ = False

LANGUAGE_CODE = 'ru-RU'
LANGUAGES = [
    ('ru', 'Russian'),
]
USE_I18N = True
USE_L10N = True
# LOCALE_PATHS = (
#     os.path.join(CORE_PATH, 'lang'),
# )

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(CORE_PATH, 'collected_static')
MEDIA_ROOT = os.path.join(CORE_PATH, 'media')
MEDIA_URL = '/media/'

# perfomance
EXCLUDE_FROM_MINIFYING = ('/admin', )
HTML_MINIFY = True
COMPRESS_PARSER = (
    # LxmlParser is the fastest available parser
    'compressor.parser.LxmlParser',
)
COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)
COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.SlimItFilter',
)
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)
