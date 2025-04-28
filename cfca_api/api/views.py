from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from cuestionario.models import PreguntaModel

@api_view()
def total_preguntas(request):
    total = PreguntaModel.objects.get_total_preguntas_activas()
    return Response({'total' : total}, status= status.HTTP_200_OK)
