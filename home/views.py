from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from catalogos.models import CatCuestionarios

@login_required
def index(request):
    nombre = request.user.first_name
    apellido = request.user.last_name

    cuestionarios = [
        'Leche y productos lacteos',
        'Carnes y productos de origen animal',
        'Verduras y Hortalizas',
        'Frutas y frutos Secos',
        'Leguminosas y cereales',
        'productos de panadería',
        'Miceláneos',
        'Bebidas',
        'Platillos preparados'
    ]
    
    opciones = """
        <button class="btn btn-primary" >Iniciar</button>
        <button class="btn btn-warning" >Reiniciar</button>
     """

    datos = {
        'nombre' : f'{nombre} {apellido}',
        'opciones' : opciones,
        'cuestionarios' : cuestionarios
    }

    return render(request, 'home.html', datos)