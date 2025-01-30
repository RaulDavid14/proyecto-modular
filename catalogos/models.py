from django.db import models

# Create your models here.
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
        
class CatEstadoCivil(CatalogoModel):
    class Meta:
        db_table = 'catalogo_estado_civil'
        verbose_name = 'Estado cívil'
        verbose_name_plural = 'Estados Civiles'
        
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
  