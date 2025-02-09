from django.db import models
from catalogos.models import DatosGenerales

class CatSituacionLaboral(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Situación Laboral")

    def __str__(self):
        return self.nombre

class CatIngresos(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Ingresos")

    def __str__(self):
        return self.nombre

class DatosSocioeconomicos(models.Model):
    datos_generales = models.OneToOneField(DatosGenerales, on_delete=models.CASCADE, verbose_name="Datos Generales")
    ingresos = models.CharField(max_length=100, verbose_name="Ingresos")
    situacion_laboral = models.CharField(max_length=100, verbose_name="Situación Laboral")

    def __str__(self):
        return f"{self.datos_generales} - {self.ingresos} - {self.situacion_laboral}"