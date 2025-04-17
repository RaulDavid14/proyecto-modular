from django.db import models

class CatalogoManager(models.Manager):
    def get_abreviacion(self, abreviacion):
        return self.filter(abreviacion = abreviacion).first()    
    

class CatOpcionMultipleEspecialManager(models.Manager):
    def selectItems(self, list_items):
        return self.filter(id__in=list_items)
