from django.shortcuts import render
from .clustering import guardar_resultados


def clustering_template(request):
    print("Se llamó a la vista clustering_template") 
    resultados = guardar_resultados()
    print("Resultados desde la vista (Template):", resultados)  
    return render(request, "clustering/clustering_results.html", {"resultados": resultados})
