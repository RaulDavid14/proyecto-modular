from django import forms
from .models import CatSexo, CatEstadoCivil, CatPoblacion, CatNivelEducativo

class DatosGeneralesForm(forms.Form):

    sexo = forms.ChoiceField(
        label='Sexo',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    estado_civil = forms.ChoiceField(
        label='Estado Civil',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    poblacion = forms.ChoiceField(
        label='Población',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    nivel_educativo = forms.ChoiceField(
        label='Nivel Educativo',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    # Sobrescribir __init__ para cargar los choices al crear el formulario
    def __init__(self, *args, **kwargs):
        super(DatosGeneralesForm, self).__init__(*args, **kwargs)
        self.fields['sexo'].choices = [(sexo.id, sexo.nombre_largo) for sexo in CatSexo.objects.all()]
        self.fields['estado_civil'].choices = [(estado.id, estado.nombre_largo) for estado in CatEstadoCivil.objects.all()]
        self.fields['poblacion'].choices = [(poblacion.id, poblacion.nombre_largo) for poblacion in CatPoblacion.objects.all()]
        self.fields['nivel_educativo'].choices = [(nivel.id, nivel.nombre_largo) for nivel in CatNivelEducativo.objects.all()]
