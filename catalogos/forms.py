from django import forms
from .models import *

class DatosGeneralesForm(forms.Form):
    sexo = forms.ModelMultipleChoiceField(
        queryset = CatSexo.objects.all(),  # Extrae las opciones del modelo Opcion
        widget = forms.CheckboxSelectMultiple,  # Cambia a Checkbox (puede ser SelectMultiple si prefieres un select)
        required = True)
    
    