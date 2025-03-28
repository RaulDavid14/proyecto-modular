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
    
    def get_cuestionario(self, preguntaModel):
        if preguntaModel is None:
            ProgresoSM.set_complete(self.id_usuario, self.cuestionario)
            template = 0
            respuestas = None
        else:
            if preguntaModel.tipo_respuesta == 1:
                template = 1
                respuestas = CatFrecuencia.objects.all()
            elif preguntaModel.tipo_respuesta == 2:
                template = 2
                respuestas = CatOpcionMultiple.objects.all()
            elif preguntaModel.tipo_respuesta == 3:
                pregunta = PreguntaSM.get_next_question(preguntaModel.no_pregunta)
                template, respuestas = self.get_cuestionario(pregunta.no_pregunta, pregunta.tipo_respuesta)
            elif preguntaModel.tipo_respuesta == 4:
                listrespuestas = []
                for key, value in preguntaModel.sig_pregunta.items():
                    listrespuestas.append(key)
                respuestas = CatOpcionMultipleEspecial.objects.filter(id__in=listrespuestas)
                template = 2
            
        return template, respuestas    

    def get_imagenes_pregunta(self, no_pregunta):
        tipo_cuestionario = CatCuestionarios.objects.filter(abreviacion = self.cuestionario).first()
        pregunta = PreguntaModel.objects.filter(no_pregunta = no_pregunta, tipo_cuestionario = tipo_cuestionario.id).first()
        dictImagen = {}
        
        if pregunta is not None:
            imagenes = []
            if pregunta.imagen_grupal:
                imagen = ImagenModel.objects.filter(pregunta__id = pregunta.id).first()
                dictImagen['grupal'] = False
                dictImagen['imagen_list'] = imagen.url
            else:
                dictImagen['grupal'] = True
                
                for imagen in ImagenModel.objects.filter(pregunta__id = pregunta.id):
                    imagenes.append(imagen.url)
                dictImagen['imagen_list'] = imagenes
            return dictImagen
        else:
            return None
    
    def get_next_question(self, id_pregunta):
        return PreguntaModel.objects.filter(id__gt=id_pregunta).order_by('id').first()
          
        
    def get_pregunta(self, pregunta):
        try:
            return PreguntaModel.objects.filter(
                no_pregunta = pregunta
                , tipo_cuestionario = self.id_cuestionario.id
            ).first()
            
        except PreguntaModel.DoesNotExist:
            return None
        except Exception:
            return None
    
    
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
        
        