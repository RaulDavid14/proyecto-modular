from django.shortcuts import render
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime
import random
import requests

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
        
        print(f'Respuestas nombre completo: {nombre_completo}')
        print(f'Respuestas situacion laboral: {situacion_laboral}')
        print(f'Respuestas ingresos: {ingresos}')
        print(f'Respuestas poblacion: {poblacion}')
        print(f'Respuestas sexo {sexo}')
        print(f'Respuestas nivel educativo {nivel_educativo}')
        
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

def obtener_resultado_simulado(user_id):
    puntaje = random.randint(0, 100)
    if puntaje >= 80:
        clasificacion = 'saludable'
    elif puntaje >= 50:
        clasificacion = 'necesita_mejorar'
    else:
        clasificacion = 'riesgo'

    return {
        'puntaje': puntaje,
        'clasificacion': clasificacion
    }

@login_required
@cache_control(no_store=True, no_cache=True, must_revalidate=True)
def informe_nutricional(request):
    try:
        # Endpoint de la API (ajústalo si estás en producción)
        url = 'http://127.0.0.1:8000/api/clustering/'  # ← Este debe apuntar a tu backend

        response = requests.get(url)
        data = response.json()

        # Buscar el resultado correspondiente al usuario actual
        resultados = data.get("clustering", [])
        resultado_usuario = next((r for r in resultados if r["user_id"] == request.user.id), None)

        if not resultado_usuario:
            return render(request, 'informe.html', {'is_completed': False})

        nivel = resultado_usuario["cluster"]

        # Convertimos a puntaje aproximado según el cluster
        puntaje_map = {
            "Bajo": 30,
            "Moderado": 60,
            "Normal": 80,
            "Excesivo": 95
        }
        puntaje = puntaje_map.get(nivel, 0)

        if puntaje >= 80:
            clasificacion = 'saludable'
        elif puntaje >= 50:
            clasificacion = 'necesita_mejorar'
        else:
            clasificacion = 'riesgo'

        context = {
            'is_completed': True,
            'puntaje': puntaje,
            'clasificacion': clasificacion,
            'now': datetime.now()
        }

    except Exception as e:
        print(f"Error al consumir la API: {e}")
        context = {'is_completed': False}

    return render(request, 'informe.html', context)
