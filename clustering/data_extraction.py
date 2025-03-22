from cuestionario.models import RespuestaModel
from catalogos.models import DatosGenerales
from cuestionario.models import PreguntaModel

def obtener_datos_usuarios():
    datos = []
    usuarios = DatosGenerales.objects.all()
    respuestas = RespuestaModel.objects.all()

    # Obtener todas las preguntas dinámicamente
    preguntas = PreguntaModel.objects.all()  # Obtener todas las preguntas
    num_preguntas = len(preguntas)  # Número total de preguntas
    print(f"Total de preguntas disponibles: {num_preguntas}")

    for usuario in usuarios:
        respuestas_usuario = respuestas.filter(id_usuario=usuario.user.id)
        respuestas_numericas = [r.id_respuesta for r in respuestas_usuario]

        # Rellenar con ceros hasta la cantidad de preguntas disponibles
        if len(respuestas_numericas) < num_preguntas:
            print(f"Usuario {usuario.id} tiene {len(respuestas_numericas)} respuestas, rellenando con ceros.")
            respuestas_numericas.extend([0] * (num_preguntas - len(respuestas_numericas)))  # Rellenar con ceros
        
        datos.append(respuestas_numericas)

    print("Datos obtenidos para clustering:", datos)
    return datos

