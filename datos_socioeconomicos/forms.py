from django import forms
from .models import DatosSocioeconomicos, CatSituacionLaboral, CatIngresos

class DatosSocioeconomicosForm(forms.ModelForm):
    ingresos = forms.ModelChoiceField(queryset=CatIngresos.objects.all(), empty_label=None)
    situacion_laboral = forms.ModelChoiceField(queryset=CatSituacionLaboral.objects.all(), empty_label=None)

    class Meta:
        model = DatosSocioeconomicos
        fields = ['ingresos', 'situacion_laboral']