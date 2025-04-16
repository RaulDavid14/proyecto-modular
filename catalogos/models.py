from django.conf import settings
from django.db import models
from .managers import CatalogoManager

class CatalogoModel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    nombre_largo = models.CharField(verbose_name='Nombre Largo', max_length=40)
    abreviacion = models.CharField(verbose_name='Nombre Corto', max_length=5)
    descripcion = models.TextField(verbose_name='Descripción')

    objects = CatalogoManager()
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.nombre_largo

    
class CatSexo(CatalogoModel):
    class Meta:
        db_table = 'catalogo_sexo'
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'
    
class CatPoblacion(CatalogoModel):
    class Meta:
        db_table = 'catalogo_poblacion'
        verbose_name = 'Población'
        verbose_name_plural = 'Tipos de Población'
    
class CatNivelEducativo(CatalogoModel):
    class Meta:
        db_table = 'catalogo_nivel_educativo'
        verbose_name = 'Nivel educativo'
        verbose_name_plural = 'Niveles educativos'
    
class CatCuestionarios(CatalogoModel):
    class Meta:
        db_table = 'catalogo_cuestionario'
        verbose_name = 'Cuestionario'
        verbose_name_plural = 'Cuestionarios'
    
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

class CatOpcionMultipleEspecial(CatalogoModel):
    class Meta:
        db_table = 'opciones_especial'
        verbose_name = 'opción especial'
        verbose_name_plural = 'opciones especiales'
    

class CatSituacionLaboral(CatalogoModel):

    class Meta:
        db_table = 'situacion_laboral'
        verbose_name = 'situación laboral'
        verbose_name_plural = 'situaciones laborales'

class CatIngresos(CatalogoModel):
    class Meta:
        db_table = 'ingresos'
        verbose_name = 'ingreso'
        verbose_name_plural = 'ingresos'

class DatosGenerales(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    poblacion = models.ForeignKey(CatPoblacion, on_delete=models.CASCADE, verbose_name="Población")
    sexo = models.ForeignKey(CatSexo, on_delete=models.CASCADE, verbose_name="Sexo")
    nivel_educativo = models.ForeignKey(CatNivelEducativo, on_delete=models.CASCADE, verbose_name="Nivel Educativo")

    def __str__(self):
        return f'Respuesta del usuario {self.user}'