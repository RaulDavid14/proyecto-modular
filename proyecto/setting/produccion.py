from .base import *

DEBUG = False

ALLOWED_HOSTS = ['cfca.pythonanywhere.com']

database = 'cfca$general'
user = 'cfca'
password = 'Cuc31.2025'
host = 'cfca.mysql.pythonanywhere-services.com'
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
