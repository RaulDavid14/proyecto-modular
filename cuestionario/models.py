from django.db import models
from .managers import PreguntaManager
class PreguntaModel(models.Model):
    texto = models.TextField(verbose_name='Pregunta')
    tipo_respuesta = models.IntegerField('tipo de preguntas')
    sig_pregunta = models.JSONField(verbose_name='siguiente pregunta', null=True, blank=True)
    tipo_cuestionario = models.IntegerField(verbose_name='tipo cuestionario')
    imagen_grupal = models.BooleanField(null=True, verbose_name='imagen grupal') # tiene imagen
    is_active = models.BooleanField(default=True, verbose_name='Activo', null=True)
    no_pregunta = models.IntegerField(verbose_name='No. Pregunta', null=True, blank=True)

    objects = PreguntaManager()

    def save(self, *args, **kwargs):
        if self.no_pregunta is None:  
            max_no_pregunta = PreguntaModel.objects.filter(tipo_cuestionario=self.tipo_cuestionario).aggregate(
                max_num=models.Max('no_pregunta')
            )['max_num']
            self.no_pregunta = (max_no_pregunta or 0) + 1  
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"id Pregunta {self.id} - Tipo Respuesta {self.tipo_respuesta} cuestionario {self.tipo_cuestionario}"

    class Meta:
        db_table = 'preguntas'
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'


class ImagenRespuestaModel(models.Model):
    nombre = models.CharField(verbose_name= 'nombre imagen', max_length=70)
    imagen = models.ImageField(upload_to='imagen_respuesta/')
    pregunta = models.ForeignKey(PreguntaModel, on_delete=models.CASCADE, related_name='imagenes', null=True)
    id_respuesta = models.IntegerField(verbose_name='ID de respuesta', null=True)
    
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        db_table = 'imagenes'
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'

class RespuestaModel(models.Model):
    id_usuario = models.IntegerField(verbose_name='usuario')
    id_cuestionario = models.IntegerField('cuestionario')
    no_pregunta = models.IntegerField('no. pregunta')
    id_respuesta = models.IntegerField('respuesta')
    
    class Meta:
        db_table = 'respuestas'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'