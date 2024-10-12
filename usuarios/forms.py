from django import forms

class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Tu usuario'
    }))

    password = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Contraseña'
    }))


class UsuarioForm(forms.Form):
    
    primer_nombre = forms.CharField(label='Primer Nombre', required=True, max_length=30, widget = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu primer nombre'}))

    segundo_nombre = forms.CharField(max_length=30, required=False, label='Segundo Nombre', widget = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu tercer nombre'}
    ))

    tercer_nombre = forms.CharField(max_length=30, required=False, label='Tercer Nombre', widget = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu segundo nombre'}
    ))

    apellido_paterno = forms.CharField(max_length=30, required=False, label='Apellido Paterno', widget = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido paterno'}
    )) 

    apellido_materno = forms.CharField(max_length=30, required=False, label='Apellido Materno', widget = forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido materno'}
    ))

    email = forms.EmailField(required = True, label = 'Correo electrónico', widget = forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'tu email '
    }))


    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'tu contraseña', 'required': 'required'}
    ))

    password_confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'confirmar contraseña', 'required': 'required'}
    ))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data 