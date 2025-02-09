from django.contrib import admin
from .models import CatSexo, CatPoblacion, CatNivelEducativo, CatCuestionarios, CatFrecuencia, CatOpcionMultiple, DatosGenerales

admin.site.register(CatSexo)
admin.site.register(CatPoblacion)
admin.site.register(CatNivelEducativo)
admin.site.register(CatCuestionarios)
admin.site.register(CatFrecuencia)
admin.site.register(CatOpcionMultiple)
admin.site.register(DatosGenerales)