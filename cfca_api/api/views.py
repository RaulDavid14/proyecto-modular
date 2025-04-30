from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListAPIView
from cuestionario.models import PreguntaModel
from catalogos.models import CatCuestionarios
from .serializers import CatCuestionariosSerializer

@api_view()
def total_preguntas(request):
    total = PreguntaModel.objects.get_total_preguntas_activas()
    return Response({'total' : total}, status= status.HTTP_200_OK)

class CuestionariosListView(ListAPIView):
    queryset = CatCuestionarios.objects.all()
    serializer_class = CatCuestionariosSerializer    