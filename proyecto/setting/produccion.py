from .base import *

DEBUG = True

ALLOWED_HOSTS = ['cfca.pythonanywhere.com']

database = 'cfca$general'
user = 'cfca'
password = 'Cuc31.2025'
host = 'cfca.mysql.pythonanywhere-services.com'
port = '3306'

APIS = {
    'cfca_api_url' : 'https://api-cfca.pythonanywhere.com/api'
    ,'timeout' : 10
}


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
