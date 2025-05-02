from django.db.models import Manager

class ImagenManager(Manager):
    def getImagenByPreguntaId(self, id_pregunta):
        return filter(pregunta__id = id_pregunta).first()