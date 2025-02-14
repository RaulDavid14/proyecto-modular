from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel, RespuestaModel
from django.db.models import Count

"""
    crear un metodo que guarde las respuestas independiente
    y configure el progres del usuario
"""
class UsuarioStateMachine():
    """
        Obtiene el listado de las primeras preguntas de cada cuestionario y crea un usuario con base a esos valores
    """
    @staticmethod
    def get_id_pregunta(id_cuestionario):
        dict_pregunta = {
            p['tipo_cuestionario'] : p['total'] 
            for p in PreguntaModel.objects.values('tipo_cuestionario').annotate(total = Count('id'))
        }
        return dict_pregunta[id_cuestionario]
    
    """
        Metodo que sirve para crear el progreso por default de
        un usuario en la base de datos.
    """    
    @staticmethod
    def create_progres(user):
        catCuestionarios = CatCuestionarios.objects.all()
        dictProgreso = {}
        
        for cuestionario in catCuestionarios:
            
            dictProgreso[cuestionario.abreviacion] = {
                'inicio' : False
                ,'id_cuestionario' : cuestionario.id
                ,'pregunta_actual' : UsuarioStateMachine.get_id_pregunta(cuestionario.id)
            }        
        progreso = ProgresoModel(id_usuario = user, cuestionarios = dictProgreso)
        progreso.save()
    
    
    @staticmethod
    def get_user_progres(id_user):
        return ProgresoModel.objects.get(id_usuario = id_user)

 
    @staticmethod
    def get_question(id_question):
        return PreguntaModel.objects.get(id = id_question)
        
        
    @staticmethod
    def get_advance_cuestionario(id_user, cuestionario):
        progreso = UsuarioStateMachine.get_user_progres(id_user = id_user)
        progreso_cuestionarios = progreso.cuestionarios
        id_cuestionario = progreso_cuestionarios[cuestionario]['id_cuestionario']
        pregunta_actual = progreso_cuestionarios[cuestionario]['pregunta_actual']
        return pregunta_actual, UsuarioStateMachine.get_question(id_cuestionario)


    
    @staticmethod
    def set_advance_cuestionario(id_user, abr_cuestionario, respuesta):
        pregunta_actual, avance_actual = UsuarioStateMachine.get_advance_cuestionario(id_user, abr_cuestionario)
        
        sig_pregunta = avance_actual.sig_pregunta[respuesta]
        respuesta_model = RespuestaModel(id_usuario = id_user, id_cuestionario = pregunta_actual, id_pregunta = avance_actual, id_respuesta = respuesta)
        respuesta_model.save()
        
        return UsuarioStateMachine.get_id_pregunta(sig_pregunta)
            
            
    """
        hacer que el metodo sea para guardar las respuestas
        y actualice el progreso del usuario
    """
    @staticmethod
    def save_response(id_user, cuestionarios):        
        ProgresoModel.objects.filter(id_usuario = id_user).update(cuestionarios = cuestionarios)
    
    """
        actualizar inicio de cuestionario a false
        obtener cuestionario a actualizar
        validar si cuestionario es true
        si es verdadero borrar registros de respuestas y actualizar por default el cuestionario.
    """
    
    @staticmethod
    def reset_progres(id_user, cuestionario):
        pregunta = UsuarioStateMachine.get_id_pregunta(cuestionario)
        progreso = UsuarioStateMachine.get_user_progres(id_user = id_user)
        #RespuestaModel.objects.filter(id_usuario = id_user).delete()
        