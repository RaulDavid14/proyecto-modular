from catalogos.models import CatCuestionarios
from .progreso_sm import ProgresoStateMachine as ProgresoSM
from django.urls import reverse

class Cuestionario:
    
    def __init__(self):
       self.__catCuestionarios = CatCuestionarios.objects.all()
        
    def get_url(self, nombre_url, abreviacion):
        return reverse(nombre_url, kwargs={'cuestionario' : abreviacion})

    def get_quiz(self, usuario):
        enlances = []
        progreso = ProgresoSM.get_progreso(usuario)
        avance = ProgresoSM.get_porcentaje_avance(usuario)
        
        for c in self.__catCuestionarios:
            disabled = 'disabled' if progreso.cuestionarios[c.abreviacion]['completado'] else ''
            iniciar = f'<a href="{self.get_url("index_cuestionario", c.abreviacion)}" class="btn btn-outline-dark flex-fill {disabled}">Iniciar</a>'
            
            cuestionario = {
                   'url': f"""
                        <div class="d-flex flex-column flex-md-row gap-2">
                            {iniciar}
                            <a href="{self.get_url('reiniciar_cuestionario', c.abreviacion)}" class="btn btn-outline-primary flex-fill">Reiniciar</a>
                        </div>
                    """
                ,'nombre_cuestionario': c.nombre_largo
                ,'progreso': avance[c.abreviacion]
            }
            enlances.append(cuestionario)
        return enlances
