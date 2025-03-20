from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
import json
import os
from django.shortcuts import render
from .models import RespuestaModel


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
    
    template, respuestas = preguntaSM.get_cuestionario(preguntaModel)
    
    if preguntaModel is None:
        data = {
            'cuestionario' : cuestionario
            ,'template' : template
        }
    else:
        data = {
            'porcentaje' : avance[cuestionario] 
            ,'cuestionario' : cuestionario
            ,'pregunta' : preguntaModel.texto
            , 'respuestas' : respuestas
            , 'template' : template
        }
    
    return render(request, 'index.html', data)

@login_required
def resultados_cuestionario(request, cuestionario):
    respuestas = RespuestaModel.objects.filter(id_cuestionario=cuestionario, id_usuario=request.user.id)
    
    total_respuestas = respuestas.count()
    if total_respuestas == 0:
        porcentajes = {"minimamente_procesado": 0, "procesado": 0, "ultra_procesado": 0}
    else:
        # Aquí se deberían hacer los cálculos para los porcentajes según el JSON de NOVA
        porcentajes = {
            "minimamente_procesado": 50,  # Datos de prueba
            "procesado": 30,
            "ultra_procesado": 20,
        }

    return render(request, "cuestionario/resultados.html", {"porcentajes": porcentajes, "cuestionario": cuestionario})

# Obtener la ruta absoluta del directorio `cuestionario`
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del JSON correctamente
JSON_PATH = os.path.join(BASE_DIR, "data", "nova.json")

# Cargar el archivo JSON
try:
    with open(JSON_PATH, "r", encoding="utf-8") as file:
        data_nova = json.load(file)
except FileNotFoundError:
    data_nova = {}  # Si el archivo no existe, evita el error
    print(f"⚠️ Error: No se encontró el archivo nova.json en {JSON_PATH}")

with open(JSON_PATH, "r", encoding="utf-8") as file:
    data_nova = json.load(file)

# Convertir el JSON en un diccionario {id_nova: clasificacion}
clasificacion_nova = {int(item["id_nova"]): item["clas_nova"].strip().lower() for item in data_nova if item["id_nova"]}

@login_required
def resultados_cuestionario(request, cuestionario):
    respuestas = RespuestaModel.objects.filter(id_usuario=request.user.id)

    total_respuestas = respuestas.count()
    if total_respuestas == 0:
        porcentajes = {"minimamente_procesado": 0, "procesado": 0, "ultra_procesado": 0}
    else:
        procesados = 0
        ultra_procesados = 0
        minimos = 0

        for respuesta in respuestas:
            id_pregunta = respuesta.id_pregunta
            if id_pregunta in clasificacion_nova:
                tipo_procesamiento = clasificacion_nova[id_pregunta]
                if "ultraprocesado" in tipo_procesamiento:
                    ultra_procesados += 1
                elif "procesado" in tipo_procesamiento:
                    procesados += 1
                else:
                    minimos += 1

        porcentajes = {
            "minimamente_procesado": (minimos / total_respuestas) * 100,
            "procesado": (procesados / total_respuestas) * 100,
            "ultra_procesado": (ultra_procesados / total_respuestas) * 100,
        }

    return render(request, "cuestionario/resultados.html", {"porcentajes": porcentajes, "cuestionario": cuestionario})