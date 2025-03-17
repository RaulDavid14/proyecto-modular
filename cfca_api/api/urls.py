from django.urls import path
from .views import *

urlpatterns = [
    path('total-preguntas', total_preguntas, name='total_preguntas'),   
]
