import cloudinary.uploader
from cuestionario.models import ImagenRespuestaModel
from imagenes.models import ImagenModel  

imagenes_a_migrar = ImagenRespuestaModel.objects.all()

for imagen_respuesta in imagenes_a_migrar:
    if imagen_respuesta.imagen:  # Verifica que la imagen existe
        print(f"Subiendo imagen: {imagen_respuesta.nombre}...")

        # Sube la imagen a Cloudinary
        resultado = cloudinary.uploader.upload(imagen_respuesta.imagen.path)

        # Crea un nuevo registro en ImagenModel con la URL de Cloudinary
        nueva_imagen = ImagenModel(
            nombre=imagen_respuesta.nombre,
            url=resultado["secure_url"],
            grupal=False,  # O ajusta según necesites
            id_respuesta=imagen_respuesta.id_respuesta,
            pregunta=imagen_respuesta.pregunta
        )
        nueva_imagen.save()

        print(f"Imagen {imagen_respuesta.nombre} subida con éxito a Cloudinary.")

print("Migración completada.")
