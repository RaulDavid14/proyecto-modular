from django.urls import path
from .views import *

urlpatterns = [
    path('generales/', index, name='generales'),    
]
