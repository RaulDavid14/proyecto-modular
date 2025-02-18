
from django.urls import path
from .views import index

urlpatterns = [
    path('generales/', index, name='generales'),
    path('', index, name='index'),
    path('editar/<int:id>/', index, name='editar_datos'),
]