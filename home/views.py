from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    nombre = request.user.first_name
    apellido = request.user.last_name
    datos = {
        'nombre' : f'{nombre} {apellido}'
    }
    return render(request, 'home.html', datos)
