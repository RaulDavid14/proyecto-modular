from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from utils.cuestionario import Cuestionario


@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def index(request):

    nombre = request.user.first_name
    apellido = request.user.last_name
    cuestionario = Cuestionario()

    datos = {
        'cuestionarios' : cuestionario.get_quiz()        
    }

    return render(request, 'home.html', datos)