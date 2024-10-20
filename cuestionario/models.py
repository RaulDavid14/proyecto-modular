from django.db import models

# Create your models here.
class PreguntaModel(models.Model):
    texto = models.TextField(verbose_name='Pregunta')
    sig_pregunta = models.IntegerField(verbose_name='siguiente pregunta')
    tipo_respuesta = models.IntegerField('tipo de preguntas')
    
