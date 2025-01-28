from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserRegistrationForm, UserLoginForm
from catalogos.models import CatCuestionarios
from .models import ProgresoModel, UserModel
import json


def create_progres(user):
    catCuestionarios = CatCuestionarios.objects.all()
    dictProgreso = {}
    
    for cuestionario in catCuestionarios:
        dictProgreso[cuestionario.abreviacion] = {
            'inicio' : False
            ,'id_cuestionario' : cuestionario.id
            ,'pregunta_actual' : 1
        }        
    progreso = ProgresoModel(id_usuario = user, cuestionarios = dictProgreso)
    progreso.save()
    
    
def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_progres(user.id)
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de inicio de sesión