from django import forms
from .models import *

class DatosSocioeconomicosForm(forms.Form):
    genero = forms.ChoiceField(
        choices=[(genero.id, genero.nombre) for genero in CatSituacionLaboral.objects.all()] , widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'sit_laboral', 'id' : 'genero'}
    ))
    
    estado_civil = forms.ChoiceField(
        choices=[(estado.id, estado.nombre) for estado in CatIngresos.objects.all()], widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'Ingresos', 'id' : 'est_civil'}
    ))