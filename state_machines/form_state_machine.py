from cuestionario.models import PreguntaModel
"""
    INICIO CUESTIONARIO
    MOSTRAR PREGUNTA
    CONTESTA PREGUNTA
    GUARDAR RESPUESTA
    SIGUIENTE PREGUNTA
"""
#extraer el inicio en la base de datos
class CuestionarioStateMachine():
    def __init__(self, user):
        self.__inicio = False
        self.__progreso = self.get_progreso()
        
        
    def get_progreso(self):
        return None
    
    def buscar_pregunta(self, id_pregunta):
        try:
            pregunta = PreguntaModel.objects.get(id=id_pregunta)
        except PreguntaModel.DoesNotExist:
            pregunta = None
        finally:
            return pregunta
    
    def get_pregunta(self, id_pregunta):
        pass