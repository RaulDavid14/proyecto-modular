from django.urls import path 
from .views import *

urlpatterns = [
    path('', index, name='dasahboard_admin'),
    path('cuestionarios/', index_cuestionario, name = 'dashboard_cuestionario'),
    path('cuestionarios/editar/<str:cuestionario>', editar_cuestionario, name = 'dashboard_editar_cuestionario'),
    path('cuestionarios/eliminar/<str:cuestionario>', eliminar_cuestionario, name = 'dashboard_eliminar_cuestionario'),
    path('preguntas/', get_preguntas, name = 'mostrar_preguntas'),
]