from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
from django.shortcuts import render

#mandar a llamar el api para borrar los datos de la base de datos del api
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

    cuerpo = preguntaSM.get_pregunta_completa(preguntaModel.no_pregunta) if preguntaModel else None
    if cuerpo is None:
        data = {
            'cuestionario': cuestionario,
            'template': 0
        }
    else:
        
        data = {
            'porcentaje': avance[cuestionario],
            'cuestionario': cuestionario,
            'pregunta': cuerpo['texto_pregunta'],
            'respuestas': cuerpo['respuestas'],
            'template': cuerpo['template'],
            'imagenes': cuerpo['imagen_grupal'] if cuerpo['imagen_grupal'] else None,
            'grupal': True if cuerpo['imagen_grupal'] else False
        }

    return render(request, 'index.html', data)