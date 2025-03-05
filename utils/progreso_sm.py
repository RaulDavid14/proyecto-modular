from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel
from django.db.models import Min

class ProgresoStateMachine():
    
    @staticmethod
    def  get_id_pregunta(id_cuestionario):
        dict_pregunta = {
            p['tipo_cuestionario'] : p['id_min']
            for p in PreguntaModel.objects.values('tipo_cuestionario').annotate(id_min = Min('id'))
        }
        return dict_pregunta.get(id_cuestionario, 0)
    
    @staticmethod
    def create_progres(user):
        catCuestionarios = CatCuestionarios.objects.all()
        dictProgreso = {}

        for cuestionario in catCuestionarios:
            dictProgreso[cuestionario.abreviacion] = {
                'inicio' : False
                ,'id_cuestionario' : cuestionario.id
                ,'pregunta_actual' : ProgresoStateMachine.get_id_pregunta(cuestionario.id)
            }
        progreso = ProgresoModel(id_usuario = user, cuestionarios = dictProgreso)
        progreso.save()    
        

        