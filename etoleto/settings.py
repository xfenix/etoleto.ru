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
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU': (
        {
            'label': u'Базовые разделы',
            'app': 'base',
            'icon': 'icon-globe'
        },
        {
            'label': u'Дополнительные разделы',
            'app': 'misc',
            'icon': 'icon-list-alt'
        },
        {
            'label': u'Пользователи',
            'app': 'auth',
        },
        '-',
        {
            'label': u'Файловый менеджер',
            'url': '/admin/filebrowser/browse/',
            'icon': 'icon-hdd',
        },
        {
            'label': u'Очистка кеша',
            'url': '/admin/clear_cache/',
            'icon': 'icon-trash clear-cache',
            'blank': True
        }
    )
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i@vi^9-trjjd(zr5j_4bf(l2^=tv*)0#6o9vwkg*(w@#fajt^v'
SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', ]

INSTALLED_APPS = (
    # django suit
    'suit',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # third party
    'compressor',
    'imagekit',
    'south',
    'flatblocks',
    'utilities',
    'filebrowser',
    'django_ace',

    # site applications
    'base',
    'misc',
)

FILEBROWSER_SUIT_TEMPLATE = True
FILEBROWSER_DIRECTORY = ''

MIDDLEWARE_CLASSES = (
    # cache for the whole site
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'base.minify.MinifyHTMLMiddleware',
    # cache for the whole site
    'django.middleware.cache.FetchFromCacheMiddleware',
    'base.minify.MarkHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'misc.context_processor.process',
)
TEMPLATE_DIRS = (
    os.path.join(CORE_PATH, 'templates'),
)
# cache templates in production
if not DEBUG:
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

ROOT_URLCONF = 'etoleto.urls'
WSGI_APPLICATION = 'etoleto.wsgi.application'

# less queries is better
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_NAME = 'etoletocookie'

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'etoleto',
            'USER': 'etoletouser',
            # super hacker password, yo
            # im so cool
            # l33t $|>3|< !$ |<00|_ = leet speak is cool
            # not cool, in fact very stupid
            # but this is very strong password
            # thanks to young people for their culture
            # sometimes it's very useful
            'PASSWORD': '$ec|_|re_$taff_0n|_y',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

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

CACHES = {
    'default': {
        # just plain old filebased cache
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache' if DEBUG else\
                   'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/etoleto_cache/',
        # we have very static site
        # and we can cache data for very long period of time
        'TIMEOUT': 86400
    }
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
STATICFILES_DIRS = (
    os.path.join(CORE_PATH, 'static'),
)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(CORE_PATH, 'collected_static')
MEDIA_ROOT = os.path.join(CORE_PATH, 'media')

# perfomance
HTML_MINIFY = True
# LxmlParser is the fastest available parser
# but htmlparser doesnt seems very slower
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
)
COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.SlimItFilter',
)

FLATPAGE_TPL_DIR = 'flatpages'
FLATPAGE_DEFAULT_TPL = 'default.html'

if not DEBUG:
    COMPRESS_ENABLED = True

if DEBUG:
    INSTALLED_APPS += (
        'devserver',
    )
