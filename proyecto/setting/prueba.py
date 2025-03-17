from .base import *

DEBUG = True

ALLOWED_HOSTS = []

APIS = {
    'url' : 'http://127.0.0.1:8000/api/'
    ,'timeout' : 10
}

database = 'CFCA'
user = 'root'
password = 'admi'
host = 'localhost'
port = '3307'

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
