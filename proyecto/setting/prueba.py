from .base import *

DEBUG = True

ALLOWED_HOSTS = []

database = 'catalogos'
user = 'root'
password = '1234'
host = 'localhost'
port = '3306'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': database,
        'USER': user,
        'PASSWORD': password,
        'HOST': host,  
        'PORT': port,  
    },
}


STATIC_URL = 'static/'
