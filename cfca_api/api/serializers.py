from rest_framework import serializers
from catalogos.models import CatCuestionarios

class CatCuestionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatCuestionarios
        fields = '__all__'