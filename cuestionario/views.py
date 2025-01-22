from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PreguntaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple
from state_machines.form_state_machine import CuestionarioStateMachine
from usuario.models import ProgresoModel

@login_required
def index(request, cuestionario):
    progresoModel = ProgresoModel.objects.get(id_usuario = request.user.id)
    print(f'Contenido progreso - {progresoModel}')
    progreso_cuestionarios = progresoModel.cuestionarios
    avance_actual = progreso_cuestionarios[cuestionario]['pregunta_actual']
    
    preguntaModel = PreguntaModel.objects.get(id=avance_actual)
      
    if request.method == 'POST':
        opcion = request.POST.get('opcion') 
        sig_pregunta = preguntaModel.sig_pregunta[opcion]
        preguntaModel = PreguntaModel.objects.get(id=sig_pregunta)
        
        progreso_cuestionarios[cuestionario]['pregunta_actual'] = sig_pregunta  
        ProgresoModel.objects.filter(id_usuario = request.user.id).update(cuestionarios=progreso_cuestionarios)
        
    
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