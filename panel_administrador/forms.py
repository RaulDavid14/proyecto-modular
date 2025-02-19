from django import forms
from cuestionario.models import PreguntaModel, ImagenRespuestaModel


class PreguntaForm(forms.ModelForm):
    class Meta:
        model = PreguntaModel
        exclude = ['id']
        
        

class ImagenRespuestaForm(forms.ModelForm):
    class Meta:
        model = ImagenRespuestaModel
        exclude = ['id']
