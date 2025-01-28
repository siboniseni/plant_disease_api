from django.urls import path
from .views import disease_detection_view

urlpatterns = [
    path("detect/", disease_detection_view, name="disease_detection"),
]
