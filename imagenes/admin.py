from django.contrib import admin
from .models import ImagenModel


# Register your models here.

@admin.register(ImagenModel)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "url")
    list_per_page = 15
    autocomplete_fields = ['pregunta']