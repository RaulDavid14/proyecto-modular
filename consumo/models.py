from django.db import models

# Create your models here.
class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    cat_opciones = models.IntegerField(verbose_name='Respuestas')
    
    
class Opcion(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    opcion = models.CharField(max_length=100, verbose_name='opción')
    
class Respuesta(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_registro = models.IntegerField()
    