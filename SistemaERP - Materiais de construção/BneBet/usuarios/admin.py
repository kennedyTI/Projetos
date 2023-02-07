from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django

# Nosso Código.
from .models import Users
from .forms import UserChangeForm, UserCreationsForm


#   Criando Janela de cargo utilizando o template do auth.
@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationsForm
    model = Users
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (('Cargo', {'fields': ('cargo',)}),)
