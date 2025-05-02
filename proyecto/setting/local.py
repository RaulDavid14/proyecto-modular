from .base import *

DEBUG = True

ALLOWED_HOSTS = []

APIS = {
    'cfca_api_url' : 'http://127.0.0.1:8001/api'
    ,'timeout' : 10
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'