from catalogos.models import CatCuestionarios
from django.urls import reverse

class Cuestionario:
    
    def __init__(self):
       self.__catCuestionarios = CatCuestionarios.objects.all()
        
    def get_url(self, nombre_url, abreviacion):
        return reverse(nombre_url, kwargs={'cuestionario' : abreviacion})
    

    def get_quiz(self):
        enlances = []

        catCuestionarios = self.__catCuestionarios
        for c in catCuestionarios:
            cuestionario = {
                   'url': f"""
                        <div class="d-flex flex-column flex-md-row gap-2">
                            <a href="{self.get_url('cuestionario', c.abreviacion)}" class="btn btn-outline-dark flex-fill">Iniciar</a>
                            <a href="{self.get_url('reiniciar_cuestionario', c.abreviacion)}" class="btn btn-outline-primary flex-fill">Reiniciar</a>
                        </div>
                    """,
                'nombre_cuestionario': c.nombre_largo
            }
            enlances.append(cuestionario)
        return enlances
