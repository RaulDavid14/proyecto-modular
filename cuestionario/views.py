from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
from django.shortcuts import render


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
    
    if preguntaModel is not None:
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
