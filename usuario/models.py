from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AdminModel(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
    class Meta:
        db_table = 'administradores'
        managed = True
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
    

class UserModel(AbstractBaseUser, PermissionsMixin):
    # Campos obligatorios
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)  # Apellido paterno
    email = models.EmailField(unique=True)
    # Campos opcionales
    second_name = models.CharField(max_length=30, blank=True, null=True)
    third_name = models.CharField(max_length=30, blank=True, null=True)
    last_name_maternal = models.CharField(max_length=30, blank=True, null=True)  # Apellido materno
    birth_date = models.DateField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = AdminModel()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Campos obligatorios para crear usuario

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'Usuarios'
        managed = True
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'