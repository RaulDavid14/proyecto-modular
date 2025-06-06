from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import RespuestaModel, PreguntaModel
from clients.client import Client

class ProgresoStateMachine():
    @staticmethod
    def get_progreso(usuario):
        return ProgresoModel.objects.get(id_usuario=usuario)    
    
   
    @staticmethod
    def is_completed_form(usuario):
        completed = []
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        
        for c in CatCuestionarios.objects.all():
            completed.append(
                progreso.cuestionarios[c.abreviacion]['completado']
            )
        
        return all(completed)        
    
    @staticmethod
    def get_porcentaje_avance(usuario):
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        ultimas_preguntas = PreguntaModel.objects.ultimas_preguntas()
        avance = {}
        for c in CatCuestionarios.objects.all():
            ultima_pregunta = ultimas_preguntas.get(tipo_cuestionario = c.id)
            
            if progreso.cuestionarios[c.abreviacion]['inicio'] is False:
                avance[c.abreviacion] = 0
            elif progreso.cuestionarios[c.abreviacion]['completado'] is True:
                avance[c.abreviacion] = 100
            else:
                avance[c.abreviacion] = round((progreso.cuestionarios[c.abreviacion]['pregunta_actual'] / ultima_pregunta['ultima_pregunta'])*100)
        
        return avance
    
    @staticmethod
    def set_complete(usuario, cuestionario):
        client = Client()
        progresoObject = ProgresoStateMachine.get_progreso(usuario)
        progresoObject.cuestionarios[cuestionario]['completado'] = True
        id_cuestionario = progresoObject.cuestionarios[cuestionario]['id_cuestionario']

        respuestas = list(RespuestaModel.objects.getRespuestasCuestionario(usuario, id_cuestionario))
        client.save_respuesta(usuario, id_cuestionario, cuestionario , respuestas)

        ProgresoModel.objects.actualizar_progreso(usuario, progresoObject.cuestionarios)
        
    @staticmethod
    def reset_progreso(usuario, cuestionario):
        cliente = Client()
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        cuestionarioModel = CatCuestionarios.objects.get(abreviacion = cuestionario)
        cliente.delete_respuesta(usuario,cuestionarioModel.id, cuestionario)        
        progreso.cuestionarios[cuestionarioModel.abreviacion]['pregunta_actual'] = 1
        progreso.cuestionarios[cuestionarioModel.abreviacion]['completado'] = False
        progreso.cuestionarios[cuestionarioModel.abreviacion]['inicio'] = False
        
        ProgresoModel.objects.actualizar_progreso(usuario, progreso.cuestionarios)
        RespuestaModel.objects.borrar_respuestas(usuario, cuestionarioModel.id)
    
    @staticmethod
    def create_progres(user):
        cliente = Client()
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
        cliente.create_progres(user)
        progreso.save()    
    