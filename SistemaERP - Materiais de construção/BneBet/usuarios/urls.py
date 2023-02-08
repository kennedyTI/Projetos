from django.urls import path

# Nosso Código.
from . import views

urlpatterns = [
    path(
        'cadastrar_usuario/',
        views.cadastrar_usuario,
        name='cadastrar_usuario'
    ),
    # Botão Excluir.
    path(
        'excluir_usuario/<str:id>/',
        views.excluir_usuario,
        name='excluir_usuario'
    )
]
