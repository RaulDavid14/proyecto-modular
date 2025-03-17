from django.db import models
from django.contrib.auth.models import User

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
        
class Alimento(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    PROCESAMIENTO_CHOICES = [
        ('minimamente_procesado', 'Mínimamente Procesado'),
        ('procesado', 'Procesado'),
        ('ultra_procesado', 'Ultra Procesado'),
    ]
    tipo_procesamiento = models.CharField(max_length=30, choices=PROCESAMIENTO_CHOICES)

    def __str__(self):
        return f"{self.nombre} - {self.get_tipo_procesamiento_display()}"
