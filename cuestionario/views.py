from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.cuestionario_sm import PreguntaSM
from utils.progreso_sm import ProgresoStateMachine as ProgresoSM
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def reiniciar(request, cuestionario):
    ProgresoSM.reset_progreso(request.user.id, cuestionario)
    return redirect('home')


class PreguntaView(LoginRequiredMixin, View):
    def get_data(self, avance, cuestionario, cuerpo_pregunta):
        if cuerpo_pregunta is None:
            return {
                'cuestionario': cuestionario,
                'template': 0
            }
        else:
            return {
                'porcentaje': avance[cuestionario],
                'cuestionario': cuestionario,
                'texto_pregunta': cuerpo_pregunta['texto_pregunta'],
                'template': cuerpo_pregunta['template'],
                'respuestas': cuerpo_pregunta['respuestas'],
                'imagen_grupal': cuerpo_pregunta['imagen_grupal'],
            }
    
    def get(self, request, cuestionario):
        preguntaSM = PreguntaSM(request.user.id, cuestionario)
        avance = ProgresoSM.get_porcentaje_avance(request.user.id)
        preguntaModel = preguntaSM.get_avance()

        cuerpo_pregunta = preguntaSM.get_cuerpo_pregunta(preguntaModel.no_pregunta) if preguntaModel else None
        
        data = self.get_data(avance, cuestionario, cuerpo_pregunta)
        return render(request, 'index.html', data)

    def post(self, request, cuestionario):
        preguntaSM = PreguntaSM(request.user.id, cuestionario)
        avance = ProgresoSM.get_porcentaje_avance(request.user.id)
        opcion = request.POST.get('opcion')
        preguntaModel = preguntaSM.save_respuesta(opcion)

        cuerpo_pregunta = preguntaSM.get_cuerpo_pregunta(preguntaModel.no_pregunta) if preguntaModel else None
        data = self.get_data(avance, cuestionario, cuerpo_pregunta)
        return render(request, 'index.html', data)
