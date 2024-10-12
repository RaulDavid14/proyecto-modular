from django.shortcuts import render
from usuarios.forms import *
from usuarios.models import *



def index(request):
    return render(request, 'landing.html')


def registrate(request):
    nuevo_usuario = UsuarioForm()

    data = {
        'form' : nuevo_usuario
    }
    return render(request, 'registrate.html', data)

def login(request):
    form = LoginForm()

    return render(request, 'login.html', {'form' : form})
