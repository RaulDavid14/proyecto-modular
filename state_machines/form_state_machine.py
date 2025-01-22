from cuestionario.models import PreguntaModel
"""
    INICIO CUESTIONARIO
    MOSTRAR PREGUNTA
    CONTESTA PREGUNTA
    GUARDAR RESPUESTA
    SIGUIENTE PREGUNTA
"""
class CuestionarioStateMachine():
    def __init__(self, user):
        self.__inicio = False
        self.__progreso = self.get_progreso()
        self.__user = user
        
        
    def get_progreso(self):
        
        pass
    
    def buscar_pregunta(self, id_pregunta):
        try:
            pregunta = PreguntaModel.objects.get(id=id_pregunta)
        except PreguntaModel.DoesNotExist:
            pregunta = None
        finally:
            return pregunta
    
    def get_pregunta(self, id_pregunta):
        pass