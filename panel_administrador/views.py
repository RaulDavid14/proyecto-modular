from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.urls import reverse

from catalogos.models import CatCuestionarios
from cuestionario.models import PreguntaModel



#mostrar las preguntas que se encuentran en el cuestionario para editarlas
def get_preguntas(request):
    preguntas = PreguntaModel.objects.all()
    page_number = request.GET.get('page', 1)
    size_number = request.GET.get('size', 10)
    paginator = Paginator(preguntas, size_number)
    
    page_obj = paginator.get_page(page_number)
    
    preguntas_data = []
    for pregunta in page_obj:
        preguntas_data.append({
            'id': pregunta.id,
            'texto': pregunta.texto,
        })
    
    response_data = {
        'preguntas': preguntas_data,
        'page': page_obj.number,
        'pages': page_obj.paginator.num_pages,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
    }
    
    return JsonResponse(response_data)

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
    
    data = {
        'nombre': cuestionario.nombre_largo,
        'descripcion': cuestionario.descripcion,
        'abreviacion': cuestionario.abreviacion,
    }
    
    return render(request, 'dashboard/cuestionario_edit/index.html', context = data)


def eliminar_cuestionario(request, cuestionario):
    cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
    return redirect('dashboard_cuestionario')