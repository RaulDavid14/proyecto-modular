from django.urls import path
from .views import *



urlpatterns = [
    path('register/', signup, name='register'),
    path('login/', login_view, name='login'),
    path('', logout_view, name='logout'),
]