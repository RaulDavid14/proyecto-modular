from cuestionario.models import PreguntaModel, RespuestaModel
from catalogos.models import CatCuestionarios
from catalogos.models import CatFrecuencia, CatOpcionMultiple
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
    
    def get_cuestionario(self, id_pregunta, tipo_respuesta):
    
        if tipo_respuesta == 1:
            template = 1
            respuestas = CatFrecuencia.objects.all()
        elif tipo_respuesta == 2:
            template = 2
            respuestas = CatOpcionMultiple.objects.all()
        elif tipo_respuesta == 3:
            pregunta = PreguntaSM.get_next_question(id_pregunta)

        elif tipo_respuesta == 4:
            template = 2
            respuestas = CatOpcionMultiple.objects.all()
            
            template, respuestas = self.get_cuestionario(pregunta.id, pregunta.tipo_respuesta)
        return template, respuestas    


    
    def get_next_question(self, id_pregunta):
        return PreguntaModel.objects.filter(id__gt=id_pregunta).order_by('id').first()
          
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
        self.progreso_cuestionario[self.cuestionario]['pregunta_actual'] = sig_pregunta.id
        
        ProgresoModel.objects.filter(id_usuario = self.id_usuario).update(
            cuestionarios = self.progreso_cuestionario
        )
        
        respuesta = RespuestaModel(
            id_usuario = self.id_usuario
            ,id_cuestionario = self.id_cuestionario.id
            ,id_respuesta = opcion
            ,id_pregunta = self.avance.id    
        )
        respuesta.save()
        
        return sig_pregunta
        
        