from django.urls import path
from .views import total_preguntas, CuestionariosListView

urlpatterns = [
    path('total-preguntas', total_preguntas, name='total_preguntas'),
    path('cuestionarios/all/', CuestionariosListView.as_view(), name='lista_cuestionarios'),   
]
