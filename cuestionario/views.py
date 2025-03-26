from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
import json
import os
from django.shortcuts import render
from .models import RespuestaModel


@login_required
def reiniciar(request, cuestionario):
    ProgresoSM.reset_progreso(request.user.id, cuestionario)
    return redirect('home')

@login_required
def index(request, cuestionario):
    preguntaSM = PreguntaSM(request.user.id, cuestionario)
    avance = ProgresoSM.get_porcentaje_avance(request.user.id)
    if request.method == 'POST':
        preguntaModel = preguntaSM.save_respuesta(request.POST.get('opcion'))
    else:
        preguntaModel = preguntaSM.get_avance()
    
    resultado = preguntaSM.get_imagenes_pregunta(no_pregunta=preguntaModel.no_pregunta)
    template, respuestas = preguntaSM.get_cuestionario(preguntaModel)
    
    if preguntaModel is None:
        data = {
            'cuestionario' : cuestionario
            ,'template' : template
        }
    else:
        data = {
            'imagenes' : resultado['imagen_list'] if resultado is not None else None
            ,'grupal' : resultado['grupal'] if resultado is not None else None
            ,'porcentaje' : avance[cuestionario] 
            ,'cuestionario' : cuestionario
            ,'pregunta' : preguntaModel.texto
            , 'respuestas' : respuestas
            , 'template' : template
        }
    
    return render(request, 'index.html', data)

@login_required
def resultados_cuestionario(request, cuestionario):
    respuestas = RespuestaModel.objects.filter(id_cuestionario=cuestionario, id_usuario=request.user.id)
    
    total_respuestas = respuestas.count()
    if total_respuestas == 0:
        porcentajes = {"minimamente_procesado": 0, "procesado": 0, "ultra_procesado": 0}
    else:
        # Aquí se deberían hacer los cálculos para los porcentajes según el JSON de NOVA
        porcentajes = {
            "minimamente_procesado": 50,  # Datos de prueba
            "procesado": 30,
            "ultra_procesado": 20,
        }

    return render(request, "cuestionario/resultados.html", {"porcentajes": porcentajes, "cuestionario": cuestionario})
