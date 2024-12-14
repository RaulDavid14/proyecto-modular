from catalogos.models import CatCuestionarios
from django.urls import reverse

class Cuestionario:
    
    def __init__(self):
       self.__catCuestionarios = CatCuestionarios.objects.all()
        
    def get_urls(self):
        return [f"/{c.abreviacion}" for c in self.__catCuestionarios]

    def get_quiz(self):
        return {
            "cuestionario" : self.get_urls(),

        }
        
