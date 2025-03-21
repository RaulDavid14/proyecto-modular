from django.db import models
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from cuestionario.models import PreguntaModel
import re  # Para extraer el public_id de la URL

class ImagenModel(models.Model):
    nombre = models.CharField(verbose_name='nombre imagen', max_length=70)
    imagen = models.ImageField(upload_to='temp/', blank=True, null=True)  
    url = models.URLField(verbose_name='url', blank=True, null=True)  
    grupal = models.BooleanField(verbose_name='imagen grupal', default=False, null=True)
    id_respuesta = models.IntegerField(verbose_name='respuesta', null=True, blank=True)
    pregunta = models.ForeignKey(PreguntaModel, on_delete=models.CASCADE, related_name='imagenes_preguntas', null=True)

    def save(self, *args, **kwargs):
        if self.imagen and not self.url:  
            uploaded_image = cloudinary.uploader.upload(self.imagen)  
            self.url = uploaded_image["secure_url"]  
            self.imagen = None  

        super().save(*args, **kwargs) 

    def delete(self, *args, **kwargs):
        """Elimina la imagen de Cloudinary antes de borrar el objeto"""
        if self.url:
            public_id = self.get_public_id()
            if public_id:
                cloudinary.uploader.destroy(public_id)  # Elimina la imagen del servidor

        super().delete(*args, **kwargs)

    def get_public_id(self):
        """Extrae el public_id desde la URL de la imagen en Cloudinary"""
        if self.url:
            match = re.search(r'/upload/(?:v\d+/)?([^/.]+)', self.url)
            if match:
                return match.group(1)
        return None

    def get_resized_image(self, width=300, height=300):
        """ Devuelve la URL de la imagen con el tamaño especificado en Cloudinary """
        if self.url:
            return self.url.replace("/upload/", f"/upload/w_{width},h_{height}/")
        return None

    class Meta:
        db_table = 'imagen_url'
        verbose_name = 'imagen'
        verbose_name_plural = 'imagenes'
