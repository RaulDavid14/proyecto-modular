from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PreguntaModel, RespuestaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple
from usuario.models import ProgresoModel
import logging

# Configuración del logger
logger = logging.getLogger(__name__)

@login_required
def index(request, cuestionario):
    try:
        logger.debug(f"Usuario: {request.user.id}, Cuestionario: {cuestionario}")

        # Obtener o crear el progreso del usuario
        progresoModel, _ = ProgresoModel.objects.get_or_create(
            id_usuario=request.user.id,
            defaults={'cuestionarios': {}}
        )
        progreso_cuestionarios = progresoModel.cuestionarios
        logger.debug(f"Progreso del usuario: {progreso_cuestionarios}")

        # Inicializar el cuestionario si no existe en el progreso
        if cuestionario not in progreso_cuestionarios:
            primera_pregunta = PreguntaModel.objects.filter(tipo_cuestionario=cuestionario).order_by('id').first()
            if primera_pregunta:
                progreso_cuestionarios[cuestionario] = {
                    'pregunta_actual': primera_pregunta.id,
                    'id_cuestionario': cuestionario
                }
                progresoModel.cuestionarios = progreso_cuestionarios
                progresoModel.save()
                logger.debug(f"Inicializado cuestionario {cuestionario} con primera pregunta ID: {primera_pregunta.id}")
            else:
                logger.error(f"No hay preguntas disponibles para el cuestionario {cuestionario}.")
                return redirect('home')

        # Obtener la pregunta actual
        avance_actual = progreso_cuestionarios[cuestionario]['pregunta_actual']
        logger.debug(f"Pregunta actual ID: {avance_actual}")
        try:
            preguntaModel = PreguntaModel.objects.get(id=avance_actual)
        except PreguntaModel.DoesNotExist:
            logger.error(f"Pregunta con ID {avance_actual} no encontrada.")
            return redirect('home')

        # Manejar la solicitud POST (guardar respuesta y avanzar)
        if request.method == 'POST':
            opcion = request.POST.get('opcion')
            opcion_str = str(opcion) if opcion else None
            logger.debug(f"Valor de 'opcion' recibido: {opcion}, tipo: {type(opcion)}")

            if opcion_str:
                try:
                    # Crear una nueva respuesta sin el campo valor_respuesta
                    RespuestaModel.objects.create(
                        id_usuario=request.user.id,
                        id_cuestionario=cuestionario,
                        id_pregunta=avance_actual,
                        id_respuesta=int(opcion_str)
                    )
                    logger.debug(f"Respuesta guardada: {opcion_str}")
                except Exception as e:
                    logger.error(f"Error al guardar la respuesta: {e}")
                    return redirect('home')

                # Avanzar a la siguiente pregunta
                sig_pregunta = preguntaModel.sig_pregunta

                # Validar que sig_pregunta sea un diccionario
                if not isinstance(sig_pregunta, dict):
                    logger.error(f"sig_pregunta no es un diccionario: {sig_pregunta}")
                    return redirect('home')

                # Convertir claves a cadenas para asegurar consistencia
                sig_pregunta = {str(k): v for k, v in sig_pregunta.items()}

                if opcion_str in sig_pregunta:
                    nueva_pregunta = sig_pregunta[opcion_str]
                    logger.debug(f'Avanzando de pregunta {avance_actual} a {nueva_pregunta}')

                    # Validar que no haya ciclos
                    if nueva_pregunta == avance_actual:
                        logger.error(f"Ciclo detectado: La pregunta {nueva_pregunta} apunta a sí misma.")
                        return redirect('home')

                    # Verificar si el cuestionario ha terminado
                    if nueva_pregunta == -1:
                        return render(request, 'finalizado.html', {'mensaje': '¡Formulario realizado con éxito!'})

                    # Actualizar el progreso del usuario
                    progreso_cuestionarios[cuestionario]['pregunta_actual'] = nueva_pregunta
                    progresoModel.cuestionarios = progreso_cuestionarios
                    progresoModel.save(update_fields=['cuestionarios'])
                    return redirect('cuestionario', cuestionario=cuestionario)
                else:
                    logger.error(f'Opción {opcion_str} no encontrada en sig_pregunta: {sig_pregunta}')
                    return redirect('home')

        # Calcular el progreso
        total_preguntas = PreguntaModel.objects.filter(tipo_cuestionario=cuestionario).count()
        progreso_porcentaje = (avance_actual / total_preguntas) * 100 if total_preguntas > 0 else 0
        logger.debug(f"Progreso: {progreso_porcentaje}%")

        # Obtener las respuestas disponibles
        if preguntaModel.tipo_respuesta == 1:
            respuestas = CatFrecuencia.objects.all()
        elif preguntaModel.tipo_respuesta == 2:
            respuestas = CatOpcionMultiple.objects.all()
        elif preguntaModel.tipo_respuesta == 3:
            # Saltar preguntas de tipo 3
            progreso_cuestionarios[cuestionario]['pregunta_actual'] += 1
            progresoModel.cuestionarios = progreso_cuestionarios
            progresoModel.save(update_fields=['cuestionarios'])
            return redirect('cuestionario', cuestionario=cuestionario)
        elif preguntaModel.tipo_respuesta == 4:
            # Saltar preguntas de tipo 4
            progreso_cuestionarios[cuestionario]['pregunta_actual'] += 1
            progresoModel.cuestionarios = progreso_cuestionarios
            progresoModel.save(update_fields=['cuestionarios'])
            return redirect('cuestionario', cuestionario=cuestionario)
        else:
            respuestas = []
            logger.warning(f"Tipo de respuesta desconocido: {preguntaModel.tipo_respuesta}")

        # Preparar el contexto para el template
        data = {
            'cuestionario': cuestionario,
            'pregunta': preguntaModel.texto,
            'respuestas': respuestas,
            'template': preguntaModel.tipo_respuesta,
            'avance': progreso_porcentaje
        }
        logger.debug(f"Contexto enviado al template: {data}")
        return render(request, 'index.html', data)

    except Exception as e:
        logger.error(f"Error inesperado en la vista: {e}")
        return redirect('home')

@login_required
def cuestionario_contestado(request, cuestionario):
    try:
        respuestas = RespuestaModel.objects.filter(id_usuario=request.user.id, id_cuestionario=cuestionario)
        datos_tabla = [
            {
                'pregunta': respuesta.id_pregunta.texto,
                'respuesta': respuesta.id_respuesta.texto
            }
            for respuesta in respuestas
        ]
        return render(request, 'cuestionario_contestado.html', {'cuestionario': cuestionario, 'datos_tabla': datos_tabla})
    except Exception as e:
        logger.error(f"Error al obtener las respuestas del cuestionario: {e}")
        return redirect('home')
