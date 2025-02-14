from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from catalogos.models import CatCuestionarios
from cuestionario.models import PreguntaModel
from django.urls import reverse

# muestra el las estadisticas de los usuarios que se registraron dentro del panel de administrador.
def index(request):
    return render(request, 'dashboard/index.html')

# muestra la lista de cuestionarios que aparecen en el cuestionario
def index_cuestionario(request):
    cuestionarios = []
    for cuestionario in CatCuestionarios.objects.all():
        editar_cuestionario = reverse('dashboard_editar_cuestionario', args=[cuestionario.abreviacion])
        eliminar_cuestionario = reverse('dashboard_eliminar_cuestionario', args=[cuestionario.abreviacion])
        acciones = f"""
            <a class="btn btn-outline-success" href="{editar_cuestionario}">Editar</a>
            <a class="btn btn-outline-danger" href="{eliminar_cuestionario}">Eliminar</a>
        """
        cuestionarios.append({
            'acciones': acciones,
            'nombre': cuestionario.nombre_largo
        })
    
    return render(request, 'dashboard/cuestionario_list/index.html', context = {'cuestionarios': cuestionarios})

def editar_cuestionario(request, cuestionario):
    cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
    return render(request, 'dashboard/cuestionario_edit/index.html')


def eliminar_cuestionario(request, cuestionario):
    cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
    return redirect('dashboard_cuestionario')