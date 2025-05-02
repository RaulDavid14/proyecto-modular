from django.urls import path
from .views import (
   reiniciar
,PreguntaView
)

urlpatterns = [
   path('<str:cuestionario>/', PreguntaView.as_view(), name = 'index_cuestionario'),
   path('reiniciar/<str:cuestionario>', reiniciar, name='reiniciar_cuestionario'),
]