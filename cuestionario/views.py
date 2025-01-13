from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#aqui se va mostrar el front que alverga las preguntas del cuestionario.
@login_required
def index(request, cuestionario):
    
    data = {
        'id' : request.user.id,
        'cuestionario' : cuestionario
    }
    
    return render(request, "index.html", data)