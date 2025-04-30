from django.urls import path
from .views import (
   reiniciar
, index_pregunta
)

urlpatterns = [
   #path("<str:cuestionario>", index, name="cuestionario"),
   path('cuestionario/<str:cuestionario>', index_pregunta, name = 'index_cuestionario'),
   path('reiniciar/<str:cuestionario>', reiniciar, name='reiniciar_cuestionario'),
]