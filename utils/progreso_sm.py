from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel, RespuestaModel
from django.db.models import Count

class ProgresoStateMachine():
    
    @staticmethod
    def  get_id_pregunta(id_cuestionario):
        dict_pregunta = {
            p['tipo_cuestionario'] : p['total']
            for p in PreguntaModel.objects.values('tipo_cuestionario').annotate(total = Count('id'))
        }
        print(dict_pregunta)
        return dict_pregunta[id_cuestionario]
    
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
        

        