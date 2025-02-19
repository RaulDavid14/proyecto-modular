from django.db import models

# Create your models here.
class PreguntaModel(models.Model):
    texto = models.TextField(verbose_name='Pregunta')
    tipo_respuesta = models.IntegerField('tipo de preguntas')
    sig_pregunta = models.JSONField(verbose_name='siguiente pregunta', null=True, blank=True)
    tipo_cuestionario = models.IntegerField(verbose_name='tipo cuestionario')

    def __str__(self):
        return f"Pregunta {self.id}"
    
    class Meta:
        db_table = 'preguntas'
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'

class RespuestaModel(models.Model):
    id_usuario = models.IntegerField(verbose_name='usuario')
    id_cuestionario = models.IntegerField('cuestionario')
    id_pregunta = models.IntegerField('no. pregunta')
    id_respuesta = models.IntegerField('respuesta')
    
    class Meta:
        db_table = 'respuestas'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        
class ImagenRespuestaModel(models.Model):
    path = models.ImageField(verbose_name='imagen', null=True, blank=True, upload_to='imagenes/')
    id_pregunta = models.ForeignKey(PreguntaModel, on_delete=models.CASCADE, related_name='imagenes')
    id_respuesta = models.IntegerField(verbose_name='respuesta')