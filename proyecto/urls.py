from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('usuario.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('cuestionario/', include('cuestionario.urls')),
    path('', include('landing.urls')),
    path('datos/', include('catalogos.urls')),
    path('panel/', include('panel_administrador.urls')),
]