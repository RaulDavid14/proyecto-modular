from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from utils.cuestionario import Cuestionario

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def index(request):
    cuestionario = Cuestionario()
    
    datos = {
        'cuestionarios': cuestionario.get_quiz(request.user.id),
        'nombre_completo': request.user.nombre_completo
    }

    return render(request, 'home.html', datos)

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def informe_nutricional(request):
    return render(request, 'informe.html')

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def ayuda(request):
    return render(request, 'ayuda.html')