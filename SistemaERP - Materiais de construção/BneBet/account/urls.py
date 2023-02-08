from django.urls import path

# Nosso Código.
from . import views

urlpatterns = [
    path(
        'entrar/',
        views.entrar,
        name='entrar'
    ),
    path(
        'sair/',
        views.sair,
        name='sair'
    ),
]
