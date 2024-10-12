from django.urls import path
from . views import *

urlpatterns = [
   path('', index, name='landing'),
   path('registrate/', registrate, name='registrate'),
   path('login/', login, name='login'), 
]
