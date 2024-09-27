from django import forms
from .models import *

#pendiente de revisar este archivo para continuar


class PreguntaForm(forms.Form):
     pregunta = forms.ChoiceField(
        choices=[(frecuencia.id, frecuencia.nombre) for frecuencia in CatFrecuencia.objects.all()] , widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'pregunta', 'id' : 'pregunta'}
    ))