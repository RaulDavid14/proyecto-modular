from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine

"""
    falta definir funcionamiento para retornar a la pregunta anterior en caso de ser necesario
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
    preguntaSM = PreguntaSM(request.user.id, cuestionario)
    preguntaModel = preguntaSM.get_avance()
    
    if request.method == 'POST':
        preguntaModel = preguntaSM.save_respuesta(request.POST.get('opcion'))

    template, respuestas = preguntaSM.get_cuestionario(preguntaModel.id, preguntaModel.tipo_respuesta)
        
    data = {
        'cuestionario' : cuestionario
        ,'pregunta' : preguntaModel.texto
        , 'respuestas' : respuestas
        , 'template' : template
    }
    
    return render(request, 'index.html', data)