from django import forms
from .models import *

#pendiente de revisar este archivo para continuar

class PreguntaForm(forms.Form):
     pregunta = forms.ChoiceField(
        choices=[(genero.id, genero.nombre) for genero in CatGenero.objects.all()] , widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'genero', 'id' : 'genero'}
    ))

