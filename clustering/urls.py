from django.urls import path
from .views import ClusteringView, clustering_template

urlpatterns = [
    path("clustering/json/", ClusteringView.as_view(), name="clustering_json"),
    path("template/", clustering_template, name="clustering_template"),
]
