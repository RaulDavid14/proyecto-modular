from django import forms
from .models import DatosSocioeconomicos, CatSituacionLaboral, CatIngresos

class DatosSocioeconomicosForm(forms.ModelForm):
    ingresos = forms.ChoiceField(choices=[(ingreso.nombre, ingreso.nombre) for ingreso in CatIngresos.objects.all()])
    situacion_laboral = forms.ChoiceField(choices=[(situacion.nombre, situacion.nombre) for situacion in CatSituacionLaboral.objects.all()])

    class Meta:
        model = DatosSocioeconomicos
        fields = ['ingresos', 'situacion_laboral']