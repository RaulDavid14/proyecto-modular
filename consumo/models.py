from django.db import models

# Create your models here.
class CatFrecuencia(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Valor")
    nombre = models.CharField(max_length=50, verbose_name="Frecuencia", help_text="Escribe el texto de la respuesta")
    abvr = models.CharField(max_length=5, verbose_name="Abreviación", help_text='Escribe la abreviación del campo')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'cat_frecuencia'  # Nombre de la tabla
        verbose_name = 'Respuesta Frecuencia'
        verbose_name_plural = 'Respuestas Frecuencia'

from django.db import models

class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True, verbose_name='valor')
    texto = models.TextField(verbose_name='Texto de la pregunta')
    tipo_respuesta = models.IntegerField(verbose_name='Tipo de Respuesta')
    pregunta = models.CharField(verbose_name='Titulo de pregunta', max_length=50, blank=True)
    grupo_imagen = models.BooleanField(default=False, verbose_name='¿Tiene grupo de imágenes?')

    def save(self, *args, **kwargs):
        # Si el campo pregunta está vacío, establece un valor por defecto basado en id_pregunta
        if not self.pregunta:
            self.pregunta = f"Pregunta {self.id_pregunta}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.pregunta

    class Meta:
        db_table = 'pregunta'
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class CatOpcion(models.Model):
    id_opcion = models.AutoField(primary_key=True, verbose_name='valor')
    nombre_opcion = models.CharField(verbose_name='opción', max_length=30)
    avbr = models.CharField(verbose_name='Abreviación', max_length=30)

    def __str__(self):
        return self.nombre_opcion

    class Meta:
        db_table = 'cat_opcion'
        verbose_name = 'opción'
        verbose_name_plural = 'opciones'


class RespuestaConsumo(models.Model):
    id_respuesta = models.AutoField(primary_key=True, verbose_name='id pregunta')
    respuestas = models.TextField(verbose_name='respuestas')
    class Meta:
        db_table = 'respuestas_consumo'
        verbose_name = 'respuesta de consumo'
        verbose_name_plural = 'respuestas de consumo'