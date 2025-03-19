from django.db import models
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from cuestionario.models import PreguntaModel

class ImagenModel(models.Model):
    nombre = models.CharField(verbose_name='nombre imagen', max_length=70)
    imagen = models.ImageField(upload_to='temp/', blank=True, null=True)  # No se usará localmente
    url = models.URLField(verbose_name='url', blank=True, null=True)  # Se llenará con la URL de Cloudinary
    grupal = models.BooleanField(verbose_name='imagen grupal', default=False, null=True)
    id_respuesta = models.IntegerField(verbose_name='respuesta', null=True, blank=True)
    pregunta = models.ForeignKey(PreguntaModel, on_delete=models.CASCADE, related_name='imagenes_preguntas', null=True)

    def save(self, *args, **kwargs):
        if self.imagen and not self.url:  
            uploaded_image = cloudinary.uploader.upload(self.imagen)  
            self.url = uploaded_image["secure_url"]  
            self.imagen = None  

        super().save(*args, **kwargs) 

    def get_resized_image(self, width=300, height=300):
        """ Devuelve la URL de la imagen con el tamaño especificado en Cloudinary """
        if self.url:
            return self.url.replace("/upload/", f"/upload/w_{width},h_{height}/")
        return None

    class Meta:
        db_table = 'imagen_url'
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'
