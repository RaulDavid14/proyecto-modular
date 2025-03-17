from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


APIS = {
    'url' : 'http://127.0.0.1:8000/api/'
    ,'timeout' : 10
}

ATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'