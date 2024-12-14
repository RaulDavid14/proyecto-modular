from django.db import models

class Catalogo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    abreviacion = models.CharField(max_length=5, verbose_name='Abreviación')
    descripcion = models.TextField(verbose_name='Descripción')
    
    class Meta:
        abstract = True

# Create your models here.
class CatSituacionLaboral(Catalogo): #herencia
   class Meta:
       verbose_name = 'Situacion Laboral' #especifica como mostrar en el panel de administrador.
       verbose_name_plural = 'Tipos de situacion laboral' #especifica como mostrar el listado.
       db_table = 'cat_situacion_laboral' #especifica el nombre el nombre de la tabla en la base de datos.

class CatIngresos(Catalogo):
    class Meta:
       verbose_name = 'Ingreso'
       verbose_name_plural = 'Cantidad de ingresos'
       db_table = 'cat_ingreso'