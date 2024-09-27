from django.shortcuts import render
from consumo.forms import *



def index(request):
    form_consumo = PreguntaForm()
    data = {
        'form' : form_consumo
    }

    return render(request, 'landing.html', context=data)