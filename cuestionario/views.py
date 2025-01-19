from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PreguntaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple

@login_required
def index(request, cuestionario):
    preguntaModel = PreguntaModel.objects.get(id=1)
    catFrecuencia = CatFrecuencia.objects.all()
    catOpcionMultiple = CatOpcionMultiple.objects.all()
    
    data = {
        'id' : request.user.id,
        'cuestionario' : cuestionario
    }
    
    if preguntaModel.tipo_cuestionario == 1:
        respuestas = catFrecuencia
    elif preguntaModel.tipo_cuestionario == 2:
        respuestas = catOpcionMultiple
        
    data = {
        'pregunta' : preguntaModel.texto
        , 'respuestas' : respuestas
    }
    
    return render(request, "index.html", data)