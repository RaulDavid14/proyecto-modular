from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel
from django.db.models import Count

class Progreso():
    @staticmethod
    def get_progreso(user):
        progreso = ProgresoModel.objects.get(id_usuario = user)
        pregunta = PreguntaModel.objects.values('tipo_cuestionario').annotate(total = Count('id'))
        
        return progreso.cuestionarios, pregunta
    
    @staticmethod
    def get_porcentaje(pregunta_actual, ultima_pregunta):
        return (pregunta_actual * 100) / ultima_pregunta 
