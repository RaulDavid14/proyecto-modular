from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('informe-nutricional', informe_nutricional, name='informe_nutricional'),
    path('ayuda', ayuda, name='ayuda'),
    path('datosgenerales', datos_generales, name='datosgenerales'),
]