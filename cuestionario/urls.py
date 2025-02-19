from django.urls import path
from .views import *

"""
   REVISAR ESTE CODIGO
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('mi_vista/', views.mi_vista, name='mi_vista'),
    # otras URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""


urlpatterns = [
   path("<str:cuestionario>", index, name="cuestionario"),
]
