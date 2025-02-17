from django.conf import settings
from django.db import models

class CatalogoModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre_largo = models.CharField(verbose_name='Nombre Largo', max_length=30)
    abreviacion = models.CharField(verbose_name='Nombre Corto', max_length=5)
    descripcion = models.TextField(verbose_name='Descripción')

    class Meta:
        abstract = True

class CatSexo(CatalogoModel):
    class Meta:
        db_table = 'catalogo_sexo'
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
    def __str__(self):
        return self.nombre_largo

class CatPoblacion(CatalogoModel):
    class Meta:
        db_table = 'catalogo_poblacion'
        verbose_name = 'Población'
        verbose_name_plural = 'Tipos de Población'
    def __str__(self):
        return self.nombre_largo

class CatNivelEducativo(CatalogoModel):
    class Meta:
        db_table = 'catalogo_nivel_educativo'
        verbose_name = 'Nivel educativo'
        verbose_name_plural = 'Niveles educativos'
    def __str__(self):
        return self.nombre_largo

class CatCuestionarios(CatalogoModel):
    class Meta:
        db_table = 'catalogo_cuestionario'
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'
    def __str__(self):
        return self.nombre_largo

class CatFrecuencia(CatalogoModel):
    class Meta:
        db_table = 'frecuencia'
        verbose_name = 'frecuencia'
        verbose_name_plural = 'frecuencias'

class CatOpcionMultiple(CatalogoModel):
    class Meta:
        db_table = 'opcion'
        verbose_name = 'opcion'
        verbose_name_plural = 'opciones'

class DatosGenerales(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    poblacion = models.ForeignKey(CatPoblacion, on_delete=models.CASCADE, verbose_name="Población")
    sexo = models.ForeignKey(CatSexo, on_delete=models.CASCADE, verbose_name="Sexo")
    nivel_educativo = models.ForeignKey(CatNivelEducativo, on_delete=models.CASCADE, verbose_name="Nivel Educativo")

    def __str__(self):
        return f"{self.user.username} - {self.poblacion.nombre_largo} - {self.sexo.nombre_largo} - {self.nivel_educativo.nombre_largo}"