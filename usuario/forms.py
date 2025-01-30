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
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Primer Nombre', 'class' : 'form-control'})
        self.fields['second_name'].widget.attrs.update({'placeholder': 'Segundo Nombre', 'class' : 'form-control'})
        self.fields['third_name'].widget.attrs.update({'placeholder': 'Tercer Nombre', 'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Apellido Paterno', 'class' : 'form-control'})
        self.fields['last_name_maternal'].widget.attrs.update({'placeholder': 'Apellido Materno', 'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'email', 'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'contraseña', 'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'contraseña', 'class' : 'form-control'})
        self.fields['birth_date'].widget = forms.DateInput(attrs={
            'placeholder': 'YYYY-MM-DD',
            'type': 'date',
            'class' : 'form-control'
        })


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'email', 'class' : 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Contraseña', 'class' : 'form-control'})
