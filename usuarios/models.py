from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UsuarioModel(AbstractUser):
    id_usuario = models.AutoField(verbose_name='ID', primary_key=True)
    primer_nombre = models.CharField(verbose_name='Primer Nombre', max_length=30)
    segundo_nombre = models.CharField(verbose_name='Segundo Nombre', max_length=30)
    tercer_nombre = models.CharField(verbose_name='Tercer Nombre', max_length=30)
    apellido_paterno = models.CharField(verbose_name='Apellido Paterno', max_length=40)
    apellido_materno = models.CharField(verbose_name='Apellido Materno', max_length=40)

    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    usuario = models.CharField(verbose_name='usuario', max_length=12)

    
    def __str__(self):
        return f'{self.apellido_paterno} {self.apellido_materno}, {self.primer_nombre} {self.segundo_nombre} {self.tercer_nombre}'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuarios'