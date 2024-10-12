from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='inicio'),
    path('success', store, name='guardar'),
    path('login', login, name='login'),
]