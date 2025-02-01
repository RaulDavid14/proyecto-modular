from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['nombre_completo', 'email', 'password1', 'password2']
        labels = {
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['nombre_completo'].widget.attrs.update({'placeholder': 'Nombre Completo', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo Electrónico', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña', 'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar Contraseña', 'class': 'form-control'})


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Correo Electrónico', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña', 'class': 'form-control'})
