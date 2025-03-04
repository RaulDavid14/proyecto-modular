from django.contrib import admin
from .models import DatosSocioeconomicos, CatSituacionLaboral, CatIngresos

admin.site.register(DatosSocioeconomicos)
admin.site.register(CatSituacionLaboral)
admin.site.register(CatIngresos)