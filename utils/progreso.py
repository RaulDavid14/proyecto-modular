from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel
from catalogos.models import CatCuestionarios


class Progreso():
    def __init__(self, user):
        self.__progreso = ProgresoModel.objects.get(id_usuario = user)
        self.__cuestionarios = CatCuestionarios.objects.all()
        
        