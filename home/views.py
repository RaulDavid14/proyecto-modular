from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from utils.cuestionario import Cuestionario
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
from datos_socioeconomicos.models import RespuestasDatosgenerales as Respuestas
from usuario.models import UserModel
from catalogos.models import (
    CatIngresos
    ,CatNivelEducativo
    ,CatPoblacion
    ,CatSexo
    ,CatSituacionLaboral
)

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
    data = {
        'is_completed' : ProgresoSM.is_completed_form(request.user.id)
    }
    return render(request, 'informe.html', data)


@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def datos_generales(request):
    respuestas = Respuestas.objects.filter(usuario=request.user.id).first()  
    usuario = UserModel.objects.get(id = request.user.id)
    if request.method == 'POST':
        nombre_completo = request.POST.get('nombre')
        situacion_laboral = request.POST.get('situacionlaboral')
        ingresos = request.POST.get('ingresos')
        poblacion = request.POST.get('poblacion')
        sexo = request.POST.get('sexo')
        nivel_educativo = request.POST.get('niveleducativo')

        if respuestas:
            usuario.nombre_completo = nombre_completo
            respuestas.situacion_laboral = situacion_laboral
            respuestas.ingresos = ingresos
            respuestas.poblacion = poblacion
            respuestas.sexo = sexo
            respuestas.nivel_educativo = nivel_educativo
        else:
            respuestas = Respuestas.objects.create(
                usuario=request.user.id,
                situacion_laboral=situacion_laboral,
                ingresos=ingresos,
                poblacion=poblacion,
                sexo=sexo,
                nivel_educativo=nivel_educativo
            )
        respuestas.save()
        usuario.save()

    datos = {
        'respuestas': respuestas,  
        'sexo': CatSexo.objects.all(),
        'situacion_laboral': CatSituacionLaboral.objects.all(),
        'nivel_educativo': CatNivelEducativo.objects.all(),
        'ingresos': CatIngresos.objects.all(),
        'poblacion': CatPoblacion.objects.all(),
        'nombre': usuario.nombre_completo
    }

    return render(request, 'datos_generales.html', datos)

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def ayuda(request):
    return render(request, 'ayuda.html')

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def informe_nutricional(request):
    is_completed = ProgresoSM.is_completed_form(request.user.id)

    if not is_completed:
        return render(request, 'informe.html', {'is_completed': False})

    puntaje = calcular_puntaje_usuario(request.user.id)
    clasificacion = clasificar_puntaje_nova(puntaje)

    context = {
        'is_completed': True,
        'puntaje': puntaje,
        'clasificacion': clasificacion,
    }

    return render(request, 'informe.html', context)