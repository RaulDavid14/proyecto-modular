from django.db import models


class PreguntaManager(models.Manager):
    def get_pregunta(self, no_pregunta, id_tipo_cuestionario):
        return self.filter(no_pregunta = no_pregunta, tipo_cuestionario = id_tipo_cuestionario).first()