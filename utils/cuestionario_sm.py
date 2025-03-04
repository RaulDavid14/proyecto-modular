from cuestionario.models import PreguntaModel, RespuestaModel
from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel


class PreguntaSM:
    def __init__(self, id_usuario, cuestionario):
        self.id_usuario = id_usuario
        self.cuestionario = cuestionario
        self.progreso_cuestionario = None
        self.progresoModel = None
        self.avance = None
        self.id_cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
        self.preguntaModel = None
            
    def set_progreso_usuario(self, usuario): 
        self.progreso_cuestionario = ProgresoModel.objects.get(id_usuario = usuario)
        
        
    def get_pregunta(self, id_pregunta):
        return PreguntaModel.objects.get(id = id_pregunta)
    
    def get_avance(self):
        self.progresoModel = ProgresoModel.objects.get(id_usuario = self.id_usuario)
        progreso = self.progresoModel.cuestionarios
        self.progreso_cuestionario = self.progresoModel.cuestionarios
        return self.get_pregunta(progreso[self.cuestionario]['pregunta_actual']) 

    def save_respuesta(self, opcion):
        self.avance = self.get_avance()
        sig_pregunta = self.get_pregunta(self.avance.sig_pregunta[opcion])
        self.progreso_cuestionario[self.cuestionario]['pregunta_actual'] = sig_pregunta
        ProgresoModel.objects.filter(id_usuario = self.id_usuario).update(
            cuestionarios = self.progreso_cuestionario
        )
        
        respuesta = RespuestaModel(
            id_usuario = self.id_usuario
            ,id_cuestionario = self.id_cuestionario
            ,id_respuesta = opcion
            ,id_pregunta = self.avance.id    
        )
        respuesta.save()
        
        return sig_pregunta
        
        
class PreguntaStateMachine:
    
    def __init__(self, id_usuario, cuestionario):
        
        self.cuestionario = cuestionario
        self.id_usuario = id_usuario
        
        self.progresoModel = ProgresoModel.objects.get(id_usuario = id_usuario)
        
        self.progreso_cuestionario = self.progresoModel.cuestionarios
        
        self.avance = self.progreso_cuestionario[cuestionario]['pregunta_actual']
        
        self.id_cuestionario = self.progreso_cuestionario[cuestionario]['id_cuestionario']
        
        self.preguntaModel = PreguntaModel.objects.get(id = self.avance)
    
    def get_avance(self):
        return self.avance
    
    def get_pregunta(self):
        print(self.preguntaModel)
        return  self.preguntaModel
    
    def save_respuesta(self, opcion):
        sig_pregunta = self.preguntaModel.sig_pregunta[opcion]
        self.preguntaModel = PreguntaModel.objects.get(id = sig_pregunta)

        self.progreso_cuestionario[self.cuestionario]['pregunta_actual'] = sig_pregunta
        
        ProgresoModel.objects.filter(id_usuario = self.id_usuario).update(cuestionarios=self.progreso_cuestionario)
        respuestaModel = RespuestaModel(id_usuario = self.id_usuario, id_cuestionario = self.id_cuestionario, id_pregunta = self.avance, id_respuesta = opcion)
        respuestaModel.save()
        