from django import forms
from .models import *

class DatosSocioeconomicosForm(forms.Form):
    situacion_laboral = forms.ChoiceField(
        label='Situación laboral',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    ingresos = forms.ChoiceField(
        label='Ingresos',
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    def __init__(self, *args, **kwargs):
        super(DatosSocioeconomicosForm, self).__init__(*args, **kwargs)
        self.fields['situacion_laboral'].choices = [(situacion_laboral.id, situacion_laboral.nombre) for situacion_laboral in CatSituacionLaboral.objects.all()]
        self.fields['ingresos'].choices = [(ingresos.id, ingresos.nombre) for ingresos in CatIngresos.objects.all()]
        