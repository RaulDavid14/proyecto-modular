from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel, RespuestaModel
from django.db.models import Min

class ProgresoStateMachine():
    @staticmethod
    def get_progreso(usuario):
        return ProgresoModel.objects.get(id=usuario)    
    
    @staticmethod
    def set_complete(usuario, cuestionario):
        progresoObject = ProgresoStateMachine.get_progreso(usuario)
        progresoObject.cuestionarios[cuestionario]['completado'] = True
        
        ProgresoModel.objects.filter(id_usuario = usuario).update(
            cuestionarios = progresoObject.cuestionarios
        )
    
    @staticmethod
    def reset_progreso(usuario, cuestionario):
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        cuestionarioModel = CatCuestionarios.objects.get(abreviacion = cuestionario)
        
        progreso.cuestionarios[cuestionarioModel.abreviacion]['pregunta_actual'] = 1
        progreso.cuestionarios[cuestionarioModel.abreviacion]['completado'] = False
        ProgresoModel.objects.filter(id_usuario = usuario).update(
            cuestionarios = progreso.cuestionarios
        )
        RespuestaModel.objects.filter(id_usuario = usuario, id_cuestionario = cuestionarioModel.id).delete()
    
    
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
    