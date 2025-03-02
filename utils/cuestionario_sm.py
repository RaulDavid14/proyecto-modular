from cuestionario.models import PreguntaModel, RespuestaModel
from usuario.models import ProgresoModel



class PreguntaStateMachine:
    
    def __init__(self, id_usuario, cuestionario):
        
        self.cuestionario = cuestionario
        self.id_usuario = id_usuario
        
        self.progresoModel = ProgresoModel.objects.get(id_usuario = id_usuario)
        
        self.progreso_cuestionario = self.progresoModel.cuestionarios
        
        self.avance = self.progreso_cuestionario[cuestionario]['pregunta_actual']
        
        self.id_cuestionario = self.progreso_cuestionario[cuestionario]['id_cuestionario']
        
        self.preguntaModel = PreguntaModel.objects.get(id = self.avance)
    
    def get_pregunta(self):
        return  self.preguntaModel
    
    def save_respuesta(self, opcion):
        sig_pregunta = self.preguntaModel.sig_pregunta[opcion]
        self.preguntaModel = PreguntaModel.objects.get(id = sig_pregunta)

        self.progreso_cuestionario[self.cuestionario]['pregunta_actual'] = sig_pregunta
        
        ProgresoModel.objects.filter(id_usuario = self.id_usuario).update(cuestionarios=self.progreso_cuestionario)
        respuestaModel = RespuestaModel(id_usuario = self.id_usuario, id_cuestionario = self.id_cuestionario, id_pregunta = self.avance, id_respuesta = opcion)
        respuestaModel.save()
        