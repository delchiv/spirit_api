from base_settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q%n1jed7+alk+#elk@^jxhvzve5)lm&3ub*9a25_d5w!!9ls!*'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

