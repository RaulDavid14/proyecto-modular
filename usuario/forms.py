from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserModel

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'second_name', 'third_name', 'last_name', 'last_name_maternal', 'birth_date', 'email', 'password1', 'password2']
        labels = {
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Primer Nombre'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido Paterno'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['birth_date'].widget.attrs.update({'placeholder': 'Fecha de Nacimiento (YYYY-MM-DD)'})

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña'})
