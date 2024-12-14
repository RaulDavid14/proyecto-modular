from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from catalogos.models import CatCuestionarios
from django.views.decorators.cache import cache_control
from utils.cuestionario import Cuestionario


@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def index(request):
    nombre = request.user.first_name
    apellido = request.user.last_name

    cuestionarios = [cuestionario.nombre_largo for cuestionario in CatCuestionarios.objects.all()]

    opciones = """
        <a href="#" class="btn btn-outline-success w-50">Iniciar</a> 
        <a href="#" class="btn btn-outline-warning w-25"> Reiniciar </a>
     """

    datos = {
        'opciones' : opciones,
        'cuestionarios' : cuestionarios
    }

    return render(request, 'home.html', datos)