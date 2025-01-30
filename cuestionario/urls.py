from django.urls import path
from .views import *

urlpatterns = [
   path("<str:cuestionario>", index, name="cuestionario"), 
]
