from django.shortcuts import render, redirect

def index(request):
    return render(request, 'landing/index.html')

def login_view(request):
    if request.method == 'POST':
        # Lógica para manejar el inicio de sesión
        return redirect('index')
    return render(request, 'landing/index.html')

def register_view(request):
    if request.method == 'POST':
        # Lógica para manejar el registro
        return redirect('index')
    return render(request, 'landing/index.html')
