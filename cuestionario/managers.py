from django.db import models


class PreguntaManager(models.Manager):
    def get_pregunta(self, no_pregunta, id_tipo_cuestionario):
        if no_pregunta is 0:
            return None
        return self.filter(no_pregunta=no_pregunta, tipo_cuestionario=id_tipo_cuestionario).first()

    def ultimas_preguntas(self):
        return self.values('tipo_cuestionario').annotate(ultima_pregunta = models.Max('no_pregunta'))


    
class RespuestaManager(models.Manager):
    def borrar_respuestas(self, id_usuario, id_cuestionario):
        self.filter(id_usuario = id_usuario, id_cuestionario = id_cuestionario).delete()