from django.urls import path
from .views import index, reiniciar, regresar_pregunta

urlpatterns = [
   path("<str:cuestionario>", index, name="cuestionario"),
   path('reiniciar/<str:cuestionario>', reiniciar, name='reiniciar_cuestionario'),
   path('regresar/<str:cuestionario>/<int:pregunta>', regresar_pregunta, name='regresar_pregunta'),
]
