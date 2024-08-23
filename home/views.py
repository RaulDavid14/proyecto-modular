from django.shortcuts import render
from datos_generales.forms import *


# Create your views here.
def index(request):
    datos_generales = DatosGeneralesForm()
    datos = {
        'datos_gen' : datos_generales
    }
    return render(request, 'home.html', context=datos)