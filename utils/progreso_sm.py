from catalogos.models import CatCuestionarios
from usuario.models import ProgresoModel
from cuestionario.models import PreguntaModel, RespuestaModel
from django.db.models import Min, Max

class ProgresoStateMachine():
    
    @staticmethod
    def reset_progreso(usuario, cuestionario):
        progreso = ProgresoModel.objects.get(id_usuario = usuario)
        cuestionario = CatCuestionarios.objects.get(abreviacion = cuestionario)
        
        progreso.cuestionarios[cuestionario.abreviacion]['pregunta_actual'] = cuestionario.id
        
        ProgresoModel.objects.filter(id_usuario = usuario).update(
            cuestionarios = progreso.cuestionarios
        )
        RespuestaModel.objects.filter(id_usuario = usuario).delete()
        
        
        
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

    @staticmethod
    def get_last_questions():
        return PreguntaModel.objects.values('tipo_cuestionario').annotate(ultimo_id=Max('id'))

    @staticmethod
    def calcular_porcentaje(usuario):
        dict_porcentajes = ProgresoStateMachine.get_last_questions()
        progreso_usuario = ProgresoModel.objects.get(id=usuario)

        ultimas_dict = {item['tipo_cuestionario']: item['ultimo_id'] for item in dict_porcentajes}

        dict_avance = {}

        print(f'QuerySet del progreso de usuario {progreso_usuario.cuestionarios}')
        print(f'QuerySet de ultimas preguntas : {dict_porcentajes}')

        for key, value in progreso_usuario.cuestionarios.items():
            id_cuestionario = value['id_cuestionario']
            pregunta_actual = value['pregunta_actual']
            ultima_pregunta = ultimas_dict.get(id_cuestionario, 0)  # Obtener última pregunta o 0 si no existe

            # Calcular porcentaje de avance
            porcentaje_avance = round((pregunta_actual / ultima_pregunta) * 100, 2) if ultima_pregunta else 0

            # Guardar en el diccionario de avance
            dict_avance[key] = {
                'pregunta_actual': pregunta_actual,
                'ultima_pregunta': ultima_pregunta,
                'porcentaje_avance': porcentaje_avance
            }

        return dict_avance
        