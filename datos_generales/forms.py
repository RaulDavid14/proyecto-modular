from django import forms
from .models import *

class DatosGeneralesForm(forms.Form):
    genero = forms.ChoiceField(
        choices=[(genero.id, genero.nombre) for genero in CatGenero.objects.all()] , widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'genero', 'id' : 'genero'}
    ))
    
    estado_civil = forms.ChoiceField(
        choices=[(estado.id, estado.nombre) for estado in CatEstadoCivil.objects.all()], widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'est_civil', 'id' : 'est_civil'}
    ))
    
    grado_estudios = forms.ChoiceField(
        choices=[(grado.id, grado.nombre) for grado in CatNivelEducativo.objects.all()], widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'estudios', 'id' : 'estudios'}
    ))
    
    poblacion = forms.ChoiceField(
        choices=[(poblacion.id, poblacion.nombre) for poblacion in CatPoblacion.objects.all()], widget=forms.RadioSelect(
        attrs={'class' : 'form-check-input', 'name' : 'poblacion', 'id' : 'poblacion'}
    ))
    
    