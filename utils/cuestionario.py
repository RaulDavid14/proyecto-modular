from catalogos.models import CatCuestionarios
from .progreso_sm import ProgresoStateMachine as ProgresoSM
from django.urls import reverse

class Cuestionario:
    
    def __init__(self):
       self.__catCuestionarios = CatCuestionarios.objects.all()
        
<<<<<<< Updated upstream
    
    def get_url(self, abreviacion):
        return reverse('cuestionario', kwargs={'cuestionario' : abreviacion})

=======
    def get_url(self, nombre_url, abreviacion):
        return reverse(nombre_url, kwargs={'cuestionario' : abreviacion})
>>>>>>> Stashed changes

    def get_quiz(self, usuario):
        enlances = []
        progreso = ProgresoSM.get_progreso(usuario)
        avance = ProgresoSM.get_porcentaje_avance(usuario)
        
        for c in self.__catCuestionarios:
            disabled = 'disabled' if progreso.cuestionarios[c.abreviacion]['completado'] else ''
            iniciar = f'<a href="{self.get_url('cuestionario', c.abreviacion)}" class="btn btn-outline-dark flex-fill {disabled}">Iniciar</a>'
            
            cuestionario = {
<<<<<<< Updated upstream
                'url': f"""
                    <a href="{self.get_url(c.abreviacion)}" class="btn btn-outline-success w-50">Iniciar</a>
                    <a href="#" class="btn btn-outline-warning w-25">Reiniciar</a>
                """,
                'nombre_cuestionario': c.nombre_largo
=======
                   'url': f"""
                        <div class="d-flex flex-column flex-md-row gap-2">
                            {iniciar}
                            <a href="{self.get_url('reiniciar_cuestionario', c.abreviacion)}" class="btn btn-outline-primary flex-fill">Reiniciar</a>
                        </div>
                    """
                ,'nombre_cuestionario': c.nombre_largo
                ,'progreso': avance[c.abreviacion]
>>>>>>> Stashed changes
            }
            enlances.append(cuestionario)
        return enlances
