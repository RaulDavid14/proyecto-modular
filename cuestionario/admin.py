from django.contrib import admin
from .models import PreguntaModel
# Register your models here.


@admin.register(PreguntaModel)
class MiModeloAdmin(admin.ModelAdmin):
    list_display = ('texto', 'id', 'tipo_cuestionario')
    ordering = ['id']
    search_fields = ('tipo_cuestionario', 'id', 'texto')
    sortable_by = ('id', 'tipo_cuestionario')
    list_per_page = 10