from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PreguntaModel, RespuestaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple
from usuario.models import ProgresoModel
from django.urls import reverse
from utils.cuestionario_sm import PreguntaStateMachine, PreguntaSM

"""
    contenido faltante para la vista
    guardar la respuesta en la base de datos de respuestas
    falta definir funcionamiento para retornar a la pregunta anterior en caso de ser necesario
    procedimiento para obtener el avance del cuestionario.
    modificar script para cargar las respuestas en la base de datos
"""

@login_required
def reiniciar(request, cuestionario):
    
    return reverse('home')
    
@login_required
def index(request, cuestionario):
    preguntaSM = PreguntaSM(request.user.id, cuestionario)
    preguntaModel = preguntaSM.get_avance()
    
    if request.method == 'POST':
        preguntaModel = preguntaSM.save_respuesta(request.POST.get('opcion'))
        
        print(f'Objeto pregunta {preguntaModel}')
            
    if preguntaModel.tipo_respuesta == 1:
        respuestas = CatFrecuencia.objects.all()
        template = 1
        
    elif preguntaModel.tipo_respuesta == 2:
        respuestas = CatOpcionMultiple.objects.all()
        template = 2
        
    data = {
        'cuestionario' : cuestionario
        ,'pregunta' : preguntaModel.texto
        , 'respuestas' : respuestas
        , 'template' : template
    }
    
    return render(request, 'index.html', data)