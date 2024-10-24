from django.shortcuts import render
from .forms import *
from datos_socioeconomicos.forms import *
# Create your views here.
def index(request):
    datos = {
        'form' : DatosGeneralesForm(),
        'economico' : DatosSocioeconomicosForm()
    }

    return render(request, 'datosgenerales.html', datos)