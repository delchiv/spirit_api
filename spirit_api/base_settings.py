"""
Django settings for spirit_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q%n1jed7+alk+#elk@^jxhvzve5)lm&3ub*9a25_d5w!!9ls!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'spirit_api.urls'

WSGI_APPLICATION = 'spirit_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE
# YOU MAY EXTEND/OVERWRITE THE DEFAULT VALUES IN YOUR settings.py FILE

ST_TOPIC_PRIVATE_CATEGORY_PK = 1
ST_UNCATEGORIZED_CATEGORY_PK = 2

ST_RATELIMIT_ENABLE = True
ST_RATELIMIT_CACHE_PREFIX = 'srl'
ST_RATELIMIT_CACHE = 'default'

ST_NOTIFICATIONS_PER_PAGE = 20

ST_MENTIONS_PER_COMMENT = 30

ST_YT_PAGINATOR_PAGE_RANGE = 3

ST_SEARCH_QUERY_MIN_LEN = 3

ST_USER_LAST_SEEN_THRESHOLD_MINUTES = 1

ST_PRIVATE_FORUM = False

ST_ALLOWED_UPLOAD_IMAGE_FORMAT = ('jpeg', 'png', 'gif')

ST_INITIAL_MIGRATION_DEPENDENCIES = []  # [('myuser', '0001_initial'), ]

#
# Django & Spirit settings defined below...
#

INSTALLED_APPS += (
    'spirit',
    # 'spirit.tests'
)

# python manage.py createcachetable spirit_cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'spirit_cache',
    },
}

AUTH_USER_MODEL = 'spirit.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'spirit.backends.user.EmailAuthBackend',
)

LOGIN_URL = 'spirit:user-login'
LOGIN_REDIRECT_URL = 'spirit:profile-update'

MIDDLEWARE_CLASSES += (
    # 'spirit.middleware.XForwardedForMiddleware',
    'spirit.middleware.TimezoneMiddleware',
    'spirit.middleware.LastIPMiddleware',
    'spirit.middleware.LastSeenMiddleware',
    'spirit.middleware.ActiveUserMiddleware',
    'spirit.middleware.PrivateForumMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


#
# Third-party apps settings defined below...
#

# django-djconfig

INSTALLED_APPS += (
    'djconfig',
)

DJC_BACKEND = 'djconfig'

CACHES.update({
    'djconfig': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-config',
    },
})

MIDDLEWARE_CLASSES += (
    'djconfig.middleware.DjConfigLocMemMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'djconfig.context_processors.config',
)

# django-haystack

INSTALLED_APPS += (
    'haystack',
)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# django-rest-framework

INSTALLED_APPS += (
    'rest_framework',
)
    
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}