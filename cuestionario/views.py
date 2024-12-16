from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request, cuestionario):

    data = {
        'id' : request.user.id,
        'cuestionario' : cuestionario
    }
    return render(request, "index.html", data)