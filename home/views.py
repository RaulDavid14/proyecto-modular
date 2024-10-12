from django.shortcuts import render, redirect
from usuarios.forms import *
from usuarios.models import *

# Create your views here.
def index(request):
    nuevo_usuario = UsuarioForm()

    data = {
        'form' : nuevo_usuario
    }
    return render(request, 'home.html', context=data)


def store(request):
    if request.method == 'POST' :
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nuevo_usuario = UsuarioModel(
                primer_nombre = form.cleaned_data['primer_nombre'],
                segundo_nombre = form.cleaned_data['segundo_nombre'],
                tercer_nombre = form.cleaned_data['tercer_nombre'],
                apellido_paterno = form.cleaned_data['apellido_paterno'],
                apellido_materno = form.cleaned_data['apellido_materno'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],  # Aquí se debe manejar la contraseña
            )

            nuevo_usuario.set_password(form.cleaned_data['password'])

            nuevo_usuario.save()

            return redirect('inicio')

def login(request):
    form = LoginForm()

    return render(request, 'login.html', {'form' : form})
   