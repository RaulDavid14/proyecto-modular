from cuestionario.models import RespuestaModel
from catalogos.models import DatosGenerales

def obtener_datos_usuarios():
    datos = []
    usuarios = DatosGenerales.objects.all()
    respuestas = RespuestaModel.objects.all()

    print("👥 Usuarios en la base de datos:", list(usuarios))  # Verifica usuarios

    for usuario in usuarios:
        respuestas_usuario = respuestas.filter(id_usuario=usuario.user.id)
        respuestas_numericas = [r.id_respuesta for r in respuestas_usuario]

        print(f"📋 Respuestas del usuario {usuario.id}:", respuestas_numericas)  # Verifica respuestas

        if respuestas_numericas:
            datos.append(respuestas_numericas)

    print("📊 Datos obtenidos para clustering:", datos)
    return datos
