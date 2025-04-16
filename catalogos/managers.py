from django.db import models

class CatalogoManager(models.Manager):
    def get_abreviacion(self, abreviacion):
        return self.filter(abreviacion = abreviacion).first()    
    

