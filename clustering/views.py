from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .clustering import guardar_resultados

class ClusteringView(View):
    def get(self, request):
        print("Se llamó a la vista ClusteringView") 
        resultados = guardar_resultados()
        print("Resultados desde la vista (JSON):", resultados)  
        return JsonResponse(resultados)

def clustering_template(request):
    print("Se llamó a la vista clustering_template") 
    resultados = guardar_resultados()
    print("Resultados desde la vista (Template):", resultados)  
    return render(request, "clustering/clustering_results.html", {"resultados": resultados})
