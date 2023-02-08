from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'admin/', 
        admin.site.urls
    ),
    #   Redireciona para a tela de Loogin.
    path(
        'account/',
        include('account.urls')
    ),
    #   Redireciona para o app usuários.
    path(
        'usuario/', 
        include('usuarios.urls')
     ),
]
