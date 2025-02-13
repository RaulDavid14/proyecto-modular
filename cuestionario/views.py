from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PreguntaModel, RespuestaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple
from usuario.models import ProgresoModel

"""
    contenido faltante para la vista
    guardar la respuesta en la base de datos de respuestas
    falta definir funcionamiento para retornar a la pregunta anterior en caso de ser necesario
    procedimiento para obtener el avance del cuestionario.
    modificar script para cargar las respuestas en la base de datos
"""


@login_required
def index(request, cuestionario):
    progresoModel = ProgresoModel.objects.get(id_usuario = request.user.id)
    
    progreso_cuestionarios = progresoModel.cuestionarios
    inicio = progreso_cuestionarios[cuestionario]['inicio']
    avance_actual = progreso_cuestionarios[cuestionario]['pregunta_actual']
    id_cuestionario = progreso_cuestionarios[cuestionario]['id_cuestionario']
    print(f'id_cuestionario {id_cuestionario}')
    preguntaModel = PreguntaModel.objects.get(id=avance_actual)
      
    if request.method == 'POST':
        opcion = request.POST.get('opcion') 
        sig_pregunta = preguntaModel.sig_pregunta[opcion]
        preguntaModel = PreguntaModel.objects.get(id=sig_pregunta)
        
        progreso_cuestionarios[cuestionario]['pregunta_actual'] = sig_pregunta  
        ProgresoModel.objects.filter(id_usuario = request.user.id).update(cuestionarios=progreso_cuestionarios)
        respuestaModel = RespuestaModel(id_usuario = request.user.id, id_cuestionario = id_cuestionario, id_pregunta = avance_actual, id_respuesta = opcion)
        respuestaModel.save()
        
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