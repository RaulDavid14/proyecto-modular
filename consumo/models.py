from django.db import models

# Create your models here.

class General(models.Model):
    id = models.Autofield(primaty_key = True)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)

class Pregunta(General):
    cat_respuestas = models.IntegerField(verbose_name="Tipo de respuesta")
    is_selected = models.IntegerField(verbose_name="siguiente pregunta")
    next_question = models.IntegerField(verbose_name="siguiente")

    class Meta:
        verbose_name = 'Pregunta' #especifica como mostrar en el panel de administrador.
        verbose_name_plural = 'Preguntas' #especifica como mostrar el listado.
        db_table = 'preguntas' #especifica el nombre el nombre de la tabla en la base de datos.     

    def __str__(self):
        return self.nombre 

    def __unicode__(self):
        return 

class catFrecuencia(General):
    avb = models.CharField(max_length=50, verbose_name = "Abreviación")


    class Meta:
        verbose_name = "Frecuencia"
        verbose_name_plural = "Opciones Frecuencia"
        db_table = 'cat_frecuencia'

    def __str__(self):
        return self.name
