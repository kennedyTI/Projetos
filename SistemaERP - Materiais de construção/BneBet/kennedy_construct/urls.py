from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #   Redireciona para o app usuários.
    path('auth/', include('usuarios.urls'))
]
