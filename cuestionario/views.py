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
def index_pregunta(request, cuestionario):
    preguntaSM = PreguntaSM(request.user.id, cuestionario)
    avance = ProgresoSM.get_porcentaje_avance(request.user.id)
    
    if request.method == 'POST':
        preguntaModel = preguntaSM.save_respuesta(request.POST.get('opcion'))
    else:
        preguntaModel = preguntaSM.get_avance()
    
    cuerpo_pregunta = preguntaSM.get_cuerpo_pregunta(preguntaModel.no_pregunta) if preguntaModel else None
    if cuerpo_pregunta is None:
        data = {
            'cuestionario': cuestionario,
            'template': 0
        }
    else:
        data = {
            'porcentaje' : avance[cuestionario]
            ,'cuestionario' : cuestionario
            ,'texto_pregunta' : cuerpo_pregunta['texto_pregunta']
            ,'template' : cuerpo_pregunta['template']
            ,'respuestas' : cuerpo_pregunta['respuestas']
            ,'imagen_grupal' : cuerpo_pregunta['imagen_grupal']
        }
    return render(request, 'index.html', data)