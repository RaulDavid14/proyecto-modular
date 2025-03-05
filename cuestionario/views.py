from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from catalogos.models import CatFrecuencia, CatOpcionMultiple
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine
"""
    crear historial de recorrido de preguntas
    revisar si es el inicio
    obtener el numero de la pregunta previamente contestada
    borrar la respuesta de la pregunta anterior
    redireccionar a la pregunta anterior
"""

@login_required
def regresar_pregunta(request, cuestionario, pregunta):
    
    return redirect('cuestionario', kwargs= {'cuestionario' : cuestionario})


@login_required
def reiniciar(request, cuestionario):
    ProgresoStateMachine.reset_progreso(request.user.id, cuestionario)
    return redirect('home')
    
@login_required
def index(request, cuestionario):
    progreso = ProgresoStateMachine.get_progreso(request.user.id)
    preguntaSM = PreguntaSM(request.user.id, cuestionario)
    preguntaModel = preguntaSM.get_avance()
    
    if request.method == 'POST':
        preguntaModel = preguntaSM.save_respuesta(request.POST.get('opcion'))
            
    if preguntaModel.tipo_respuesta == 1:
        respuestas = CatFrecuencia.objects.all()
        template = 1
        
    elif preguntaModel.tipo_respuesta == 2:
        respuestas = CatOpcionMultiple.objects.all()
        template = 2
        
    data = {
        'cuestionario' : cuestionario
        ,'pregunta' : preguntaModel.texto
        ,'respuestas' : respuestas
        ,'template' : template
        ,'inicio ' : progreso.cuestionarios[cuestionario]['inicio']
    }
    
    return render(request, 'index.html', data)