from django.urls import path 
from .views import *

urlpatterns = [
    path('', index, name='dasahboard_admin'),
    path('cuestionarios/', index_cuestionario, name = 'dashboard_cuestionario'),
    path('cuestionarios/editar/<str:cuestionario>', editar_cuestionario, name = 'dashboard_editar_cuestionario'),
    path('cuestionarios/eliminar/<str:cuestionario>', eliminar_cuestionario, name = 'dashboard_eliminar_cuestionario'),
    path('preguntas/<int:id_cuestionario>', get_preguntas, name = 'mostrar_preguntas'),
    path('preguntas/editar/<int:id_pregunta>', editar_pregunta, name = 'editar_pregunta'),
]