from django.test import TestCase
from django.test import TestCase
from .models import DatosGenerales, CatSexo, CatPoblacion, CatNivelEducativo
from datos_socioeconomicos.models import DatosSocioeconomicos, CatSituacionLaboral, CatIngresos

class DatosGeneralesTestCase(TestCase):
    def setUp(self):
        self.sexo = CatSexo.objects.create(nombre_largo="Masculino", abreviacion="M", descripcion="Masculino")
        self.poblacion = CatPoblacion.objects.create(nombre_largo="Urbana", abreviacion="U", descripcion="Urbana")
        self.nivel_educativo = CatNivelEducativo.objects.create(nombre_largo="Primaria", abreviacion="P", descripcion="Primaria")
        self.situacion_laboral = CatSituacionLaboral.objects.create(nombre="Empleado", abreviacion="E", descripcion="Empleado")
        self.ingresos = CatIngresos.objects.create(nombre="Alto", abreviacion="A", descripcion="Alto")

    def test_datos_generales_creation(self):
        datos_generales = DatosGenerales.objects.create(
            poblacion=self.poblacion,
            sexo=self.sexo,
            nivel_educativo=self.nivel_educativo
        )
        self.assertEqual(datos_generales.poblacion, self.poblacion)
        self.assertEqual(datos_generales.sexo, self.sexo)
        self.assertEqual(datos_generales.nivel_educativo, self.nivel_educativo)

    def test_datos_socioeconomicos_creation(self):
        datos_generales = DatosGenerales.objects.create(
            poblacion=self.poblacion,
            sexo=self.sexo,
            nivel_educativo=self.nivel_educativo
        )
        datos_socioeconomicos = DatosSocioeconomicos.objects.create(
            datos_generales=datos_generales,
            ingresos=self.ingresos,
            situacion_laboral=self.situacion_laboral
        )
        self.assertEqual(datos_socioeconomicos.datos_generales, datos_generales)
        self.assertEqual(datos_socioeconomicos.ingresos, self.ingresos)
        self.assertEqual(datos_socioeconomicos.situacion_laboral, self.situacion_laboral)

# Create your tests here.
