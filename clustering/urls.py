from django.urls import path
from .views import clustering_template

urlpatterns = [
    path("template/", clustering_template, name="clustering_template"),
]
