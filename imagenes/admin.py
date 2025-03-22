from django.contrib import admin
from .models import ImagenModel


# Register your models here.

@admin.register(ImagenModel)
class ImagenAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pregunta']