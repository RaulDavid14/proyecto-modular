from catalogos.models import CatCuestionarios
from django.urls import reverse

class Cuestionario:
    
    def __init__(self):
       self.__catCuestionarios = CatCuestionarios.objects.all()
        
    
    def get_url(self, abreviacion):
        return reverse('cuestionario', kwargs={'cuestionario' : abreviacion})


    def get_quiz(self):
        enlances = []

        catCuestionarios = self.__catCuestionarios
        for c in catCuestionarios:
            cuestionario = {
                'url': f"""
                    <a href="{self.get_url(c.abreviacion)}" class="btn btn-outline-success w-50">Iniciar</a>
                    <a href="#" class="btn btn-outline-warning w-25">Reiniciar</a>
                """,
                'nombre_cuestionario': c.nombre_largo
            }
            enlances.append(cuestionario)
        return enlances