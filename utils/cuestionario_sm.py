from cuestionario.models import PreguntaModel, RespuestaModel
from usuario.models import ProgresoModel
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
from imagenes.models import ImagenModel
from catalogos.models import (
    CatFrecuencia
    ,CatOpcionMultiple
    ,CatCuestionarios
    ,CatOpcionMultipleEspecial
)

"""
agregar preguntas perzonalizadas
agregar validacion para mostrar imagen en base a la pregunta

"""

class PreguntaSM():
    def __init__(self, id_usuario, cuestionario):
        self.id_usuario = id_usuario
        self.cuestionario = cuestionario
        self.progreso_cuestionario = None
        self.progresoModel = None
        self.avance = None
        self.id_cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
        self.preguntaModel = None
        
    # REVISAR POR QUE SE SALTA HASTA EL FINAL
    def get_pregunta(self, no_pregunta):
        try:
            preguntaModel = PreguntaModel.objects.get_pregunta(no_pregunta, self.id_cuestionario.id)
            
            if preguntaModel.is_active is True:
                return preguntaModel
            else:
                return self.get_pregunta(no_pregunta + 1)
            
        except PreguntaModel.DoesNotExist:
            print("La pregunta no fue encontrada")
            return None
        except Exception as exception:
            print(f"Error interno del servidor {str(exception)}")
            return None
    """
        TODO:
        -   Revisar el template para ver si se mandan las imagenes
        -   Ver como se mandan las imagenes desde la vista.
        -   Revisar si la pregunta no tiene grupal nulo y se encuentra activa. 
    """
    def get_pregunta_completa(self, no_pregunta):
        tipo_cuestionario = CatCuestionarios.objects.get_abreviacion(self.cuestionario)
        pregunta = PreguntaModel.objects.get_pregunta(no_pregunta, tipo_cuestionario.id)

        if pregunta is None:
            ProgresoSM.set_complete(self.id_usuario, self.cuestionario)
            return {
                'template': 0,
                'pregunta_id': None,
                'texto_pregunta': None,
                'imagen_grupal': None,
                'respuestas': []
            }

        TIPOS_RESPUESTA = {
            1: {
                'template': 1,
                'respuestas': lambda: CatFrecuencia.objects.all(),
            },
            2: {
                'template': 2,
                'respuestas': lambda: CatOpcionMultiple.objects.all(),
            },
            4: {
                'template': 2,
                'respuestas': lambda: CatOpcionMultipleEspecial.objects.filter(
                    id__in=list(pregunta.sig_pregunta.keys()) if pregunta.sig_pregunta else []
                )
            }
        }

        config = TIPOS_RESPUESTA[pregunta.tipo_respuesta]
        respuestas_raw = config['respuestas']()

        imagen_grupal = None
        imagenes_por_respuesta = {}

        for imagen in pregunta.imagenes_preguntas.all():
            if pregunta.imagen_grupal:
                imagen_grupal = imagen.url
            elif imagen.id_respuesta:
                imagenes_por_respuesta[imagen.id_respuesta] = imagen.url

        respuestas_formateadas = []
        for r in respuestas_raw:
            respuesta = {
                "id": r.id,
                "texto": getattr(r, "texto", getattr(r, "nombre_largo", str(r)))
            }
            if pregunta.tipo_respuesta == 4 and r.id in imagenes_por_respuesta:
                respuesta["imagen"] = imagenes_por_respuesta[r.id]
            respuestas_formateadas.append(respuesta)

        return {
            'template': config['template'],
            'pregunta_id': pregunta.id,
            'texto_pregunta': pregunta.texto,
            'imagen_grupal': imagen_grupal,
            'respuestas': respuestas_formateadas
        }

    def get_avance(self):
        try:
            self.progresoModel = ProgresoModel.objects.get(id_usuario=self.id_usuario)
            progreso = self.progresoModel.cuestionarios
            self.progreso_cuestionario = progreso

            if self.cuestionario not in progreso or 'pregunta_actual' not in progreso[self.cuestionario]:
                return None  
            
            return self.get_pregunta(progreso[self.cuestionario]['pregunta_actual'])
        except ProgresoModel.DoesNotExist:
            return None  
        except Exception as e:
            print(f"Error en get_avance: {e}")
            return None

    def get_avances(self):
        try:
            self.progresoModel = ProgresoModel.objects.get(id_usuario=self.id_usuario)
            progreso = self.progresoModel.cuestionarios
            self.progreso_cuestionario = progreso

            if self.cuestionario not in progreso or 'pregunta_actual' not in progreso[self.cuestionario]:
                return None  
            
            return None #self.get_pregunta(progreso[self.cuestionario]['pregunta_actual'])
        except ProgresoModel.DoesNotExist:
            return None  
        except Exception as e:
            print(f"Error en get_avance: {e}")
            return None

    
    def save_respuesta(self, opcion):
        self.avance = self.get_avance()
        if self.progreso_cuestionario[self.cuestionario]['inicio'] is False:
            self.progreso_cuestionario[self.cuestionario]['inicio'] = True
        
        try:
            respuesta = RespuestaModel(
                id_usuario=self.id_usuario,
                id_cuestionario=self.id_cuestionario.id,
                id_respuesta=opcion,
                no_pregunta=self.avance.no_pregunta    
            )
            respuesta.save()
        except Exception as e:
            print(f"Error al guardar la respuesta: {e}")
            return None

        if self.avance is None or not hasattr(self.avance, 'sig_pregunta') or opcion not in self.avance.sig_pregunta:
            return None  
        
        sig_pregunta = self.get_pregunta(self.avance.sig_pregunta[opcion])

        if sig_pregunta is None:
            return None  
        
        self.progreso_cuestionario[self.cuestionario]['pregunta_actual'] = sig_pregunta.no_pregunta
        
        
        try:
            ProgresoModel.objects.filter(id_usuario=self.id_usuario).update(
                cuestionarios=self.progreso_cuestionario
            )
        except Exception as e:
            print(f"Error al actualizar el progreso: {e}")
            return None
        
        
        return sig_pregunta