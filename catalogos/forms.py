from django import forms
from .models import DatosGenerales, CatSexo, CatPoblacion, CatNivelEducativo

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model = DatosGenerales
        fields = ['sexo', 'poblacion', 'nivel_educativo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sexo'].choices = [(sexo.nombre_largo, sexo.nombre_largo) for sexo in CatSexo.objects.all()]
        self.fields['poblacion'].choices = [(poblacion.nombre_largo, poblacion.nombre_largo) for poblacion in CatPoblacion.objects.all()]
        self.fields['nivel_educativo'].choices = [(nivel.nombre_largo, nivel.nombre_largo) for nivel in CatNivelEducativo.objects.all()]