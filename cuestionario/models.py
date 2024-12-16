from django.db import models

# Create your models here.
class PreguntaModel(models.Model):
    texto = models.TextField(verbose_name='Pregunta')
    tipo_respuesta = models.IntegerField('tipo de preguntas')
    sig_pregunta = models.JSONField(verbose_name='siguiente pregunta')
    tipo_cuestionario = models.IntegerField(verbose_name='tipo cuestionario')

    class Meta:
        db_table = 'preguntas'
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'


class RespuestaModel(models.Model):

    id_usuario = models.IntegerField(verbose_name='usuario')
    id_pregunta = models.IntegerField(verbose_name='pregunta')
    id_cuestionario = models.IntegerField(verbose_name='cuestionario')
    id_respuesta = models.IntegerField(verbose_name='respuesta')

    class Meta:
        db_table = 'respuestas'
        verbose_name = 'respuesta'
        verbose_name_plural = 'respuestas'