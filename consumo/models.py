from django.db import models

# Create your models here.
class CatFrecuencia(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Valor")
    nombre = models.CharField(max_length=50, verbose_name="Frecuencia", help_text="Escribe el texto de la respuesta")
    abvr = models.CharField(max_length=5, verbose_name="Abreviación", help_text='Escribe la abreviación del campo')

    class Meta:
        db_table = 'cat_frecuencia'  # Nombre de la tabla
        verbose_name = 'Respuesta Frecuencia'
        verbose_name_plural = 'Respuestas Frecuencia'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True, verbose_name='ID Pregunta')
    texto = models.TextField(verbose_name='Texto de la pregunta')
    tipo_respuesta = models.IntegerField(verbose_name='Tipo de Respuesta')  # IntegerField es lo correcto
    grupo_imagen = models.BooleanField(default=False, verbose_name='¿Tiene grupo de imágenes?')  # Cambiado a BooleanField

    class Meta:
        db_table = 'pregunta'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class CatImagen(models.Model):
    id_imagen = models.AutoField(primary_key=True, verbose_name="ID Imagen")
    
    class Meta:
        db_table = 'cat_imagen'
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'  # Corregido verbose_name_plural
