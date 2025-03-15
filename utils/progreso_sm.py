from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel, RespuestaModel
from django.db.models import Min

class ProgresoStateMachine():
    
    @staticmethod
    def count_questions(cuestionario):
        cuestionarioModel = CatCuestionarios.objects.get(abreviacion = cuestionario)
        return PreguntaModel.objects.filter(tipo_cuestionario = cuestionarioModel.id).count()
        
    
    @staticmethod
    def reset_progreso(usuario, cuestionario):
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
        
        progreso.cuestionarios[cuestionario.abreviacion]['pregunta_actual'] = 1
        
        ProgresoModel.objects.filter(id_usuario = usuario).update(
            cuestionarios = progreso.cuestionarios
        )
        RespuestaModel.objects.filter(id_usuario = usuario).delete()
        
    @staticmethod
    def get_progreso(usuario):
        return ProgresoModel.objects.get(id=usuario)    
    
    @staticmethod
    def get_id_pregunta(id_cuestionario):
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
                ,'pregunta_actual' : 1
                ,'completado' : False
            }
        progreso = ProgresoModel(id_usuario = user, cuestionarios = dictProgreso)
        progreso.save()    

    @staticmethod
    def get_last_question(id_cuestionario):
        id_pregunta = PreguntaModel.objects.filter(tipo_cuestionario = id_cuestionario).first()
        return id_pregunta.id
