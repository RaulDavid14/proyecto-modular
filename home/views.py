from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from catalogos.models import CatCuestionarios
from django.views.decorators.cache import cache_control

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def index(request):
    nombre = request.user.first_name
    apellido = request.user.last_name

    cuestionarios = [cuestionario.nombre_largo for cuestionario in CatCuestionarios.objects.all()]

    opciones = """
        <button class="btn btn-outline-success w-50" >Iniciar</button>
        <button class="btn btn-outline-warning w-25" >Reiniciar</button>
     """

    datos = {
        'opciones' : opciones,
        'cuestionarios' : cuestionarios
    }

    return render(request, 'home.html', datos)