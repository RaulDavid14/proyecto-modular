from django.db import models

class Catalogo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    abreviacion = models.CharField(max_length=5, verbose_name='Abreviación')
    descripcion = models.TextField(verbose_name='Descripción')
    
    class Meta:
        abstract = True


# Create your models here.
class CatGenero(Catalogo): #herencia
   class Meta:
       verbose_name = 'Género' #especifica como mostrar en el panel de administrador.
       verbose_name_plural = 'Géneros' #especifica como mostrar el listado.
       db_table = 'cat_genero' #especifica el nombre el nombre de la tabla en la base de datos.

class CatEstadoCivil(Catalogo):
    class Meta:
       verbose_name = 'Género'
       verbose_name_plural = 'Géneros'
       db_table = 'cat_estado_civil'
           
class CatPoblacion(Catalogo):
    class Meta:
       verbose_name = 'Población'
       verbose_name_plural = 'Tipos Población'
       db_table = 'cat_poblacion'

class CatNivelEducativo(Catalogo):
    class Meta:
       verbose_name = 'Nivel Educativo'
       verbose_name_plural = 'Niveles educativos'
       db_table = 'cat_nivel_educativo'