from django.db import models
from catalogos.models import DatosGenerales

class CatSituacionLaboral(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Situación Laboral")
    abreviacion = models.CharField(max_length=10, blank=True, null=True, verbose_name="Abreviación")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class CatIngresos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Ingresos")
    abreviacion = models.CharField(max_length=10, blank=True, null=True, verbose_name="Abreviación")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class RespuestasDatosgenerales(models.Model):
    usuario = models.IntegerField()
    situacion_laboral = models.IntegerField()
    ingresos = models.IntegerField()
    sexo = models.IntegerField()
    poblacion = models.IntegerField()
    nivel_educativo = models.IntegerField()
    
    class Meta: 
        db_table = 'respuestas_datos_generales'

class DatosSocioeconomicos(models.Model):
    datos_generales = models.OneToOneField(
        DatosGenerales, 
        on_delete=models.CASCADE, 
        verbose_name="Datos Generales"
    )
    ingresos = models.ForeignKey(
        CatIngresos, 
        on_delete=models.CASCADE, 
        verbose_name="Ingreso"
    )
    situacion_laboral = models.ForeignKey(
        CatSituacionLaboral, 
        on_delete=models.CASCADE, 
        verbose_name="Situación Laboral"
    )

    def __str__(self):
        return f"{self.datos_generales} - {self.ingresos} - {self.situacion_laboral}"
