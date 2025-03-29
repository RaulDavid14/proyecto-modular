from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('email', 'nombre_completo', 'is_staff', 'is_active')  # Campos visibles en la lista de admin
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('nombre_completo', 'birth_date')}),
        ('Permisos', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nombre_completo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    
    search_fields = ('email', 'nombre_completo')
    ordering = ('email',)

admin.site.register(UserModel, CustomUserAdmin)
