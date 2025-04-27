from django.db import models

class ProgresoManager(models.Manager):
    def actualizar_progreso(self, id_usuario, cuestionario):
        self.filter(id_usuario = id_usuario).update(
            cuestionarios = cuestionario
        )
        