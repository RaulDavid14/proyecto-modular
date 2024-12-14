from django.urls import path
from .views import *

urlpatterns = [
   path("cuestionario/<str:cuestionario>", index, name="cuestionario"), 
]
