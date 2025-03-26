import os
import json
from django.conf import settings
from cuestionario.models import RespuestaModel

# Cargar datos desde el archivo JSON
def cargar_datos_nova():
    ruta_archivo = os.path.join(settings.BASE_DIR, 'utils', 'NOVA.json')
    with open(ruta_archivo, encoding='utf-8') as f:
        return json.load(f)

# Calcular el puntaje de un usuario
def calcular_puntaje_usuario(user_id):
    respuestas = RespuestaModel.objects.filter(id_usuario=user_id)
    datos_nova = cargar_datos_nova()

    puntaje = 0
    total_respuestas_validas = 0

    for respuesta in respuestas:
        for item in datos_nova:
            if item['id_pregunta'] == respuesta.no_pregunta and item['id_respuesta'] == respuesta.id_respuesta:
                clasificacion = item['clasificacion_nova'].lower()

                # Asignar puntaje (ajustable)
                if clasificacion == 'grupo 1':
                    puntaje += 3
                elif clasificacion == 'grupo 2':
                    puntaje += 2
                elif clasificacion == 'grupo 3':
                    puntaje += 1
                elif clasificacion == 'grupo 4':
                    puntaje += 0

                total_respuestas_validas += 1
                break  # Evita múltiples matches

    # Calcular promedio
    if total_respuestas_validas == 0:
        return 0  # Evita división por cero

    max_puntaje = total_respuestas_validas * 3  # 3 es el máximo por pregunta
    porcentaje = int((puntaje / max_puntaje) * 100)
    return porcentaje

# Clasificar según el puntaje
def clasificar_puntaje_nova(puntaje):
    if puntaje >= 80:
        return 'saludable'
    elif puntaje >= 50:
        return 'necesita_mejorar'
    else:
        return 'pobre'
