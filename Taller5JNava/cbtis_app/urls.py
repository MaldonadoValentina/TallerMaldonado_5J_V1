from django.urls import path
from . import views

urlpatterns = [
    path("", views.ver_lista, name="ver_lista"),
]