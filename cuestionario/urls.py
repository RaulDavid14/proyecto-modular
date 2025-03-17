from django.urls import path
from .views import index, reiniciar

urlpatterns = [
   path("<str:cuestionario>", index, name="cuestionario"),
   path('reiniciar/<str:cuestionario>', reiniciar, name='reiniciar_cuestionario'),
   path('resultados/<str:cuestionario>/', resultados_cuestionario, name='resultados'),
]
