from django.urls import path

# Nosso Código.
from . import views

urlpatterns = [
    path('cadastrar_vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
]