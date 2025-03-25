from django.contrib import admin
from .models import (
CatSexo
, CatPoblacion
, CatNivelEducativo
, CatCuestionarios
, CatFrecuencia
, CatOpcionMultiple
, CatOpcionMultipleEspecial
, CatIngresos
, CatSituacionLaboral
)

admin.site.register(CatSexo)
admin.site.register(CatPoblacion)
admin.site.register(CatNivelEducativo)
admin.site.register(CatCuestionarios)
admin.site.register(CatFrecuencia)
admin.site.register(CatOpcionMultiple)
admin.site.register(CatOpcionMultipleEspecial)
admin.site.register(CatSituacionLaboral)
admin.site.register(CatIngresos)