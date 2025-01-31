from cuestionario.models import PreguntaModel
from catalogos.models import CatFrecuencia, CatOpcionMultiple

class Pregunta:
    def __init__(self):
        self.opciones_frecuencias = CatFrecuencia.objects.all()
        self.opciones = CatOpcionMultiple.objects.all()
    
    
    def get_pregunta(self, id_pregunta):
        try:
            pregunta = PreguntaModel.objects.get(id = id_pregunta)
        except PreguntaModel.DoesNotExist:
            pregunta = None
        finally:
            return pregunta
     