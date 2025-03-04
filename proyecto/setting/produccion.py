from .base import *

DEBUG = True

ALLOWED_HOSTS = []

user = 'root'
password = '1234'
host = 'localhost'
port = '3306'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'catalogos',
        'USER': user,
        'PASSWORD': password,
        'HOST': host,  
        'PORT': port,  
    },
}


STATIC_URL = 'static/'
