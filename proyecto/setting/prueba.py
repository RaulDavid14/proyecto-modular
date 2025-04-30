from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


APIS = {
    'cfca_api_url' : 'http://127.0.0.1:8001/api'
    ,'timeout' : 10
}


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
