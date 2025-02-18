from django import forms
from .models import DatosGenerales, CatSexo, CatPoblacion, CatNivelEducativo

class DatosGeneralesForm(forms.ModelForm):
    class Meta:
        model = DatosGenerales
        fields = ['sexo', 'poblacion', 'nivel_educativo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sexo'].queryset = CatSexo.objects.all()
        self.fields['sexo'].empty_label = None
        self.fields['poblacion'].queryset = CatPoblacion.objects.all()
        self.fields['poblacion'].empty_label = None
        self.fields['nivel_educativo'].queryset = CatNivelEducativo.objects.all()
        self.fields['nivel_educativo'].empty_label = None