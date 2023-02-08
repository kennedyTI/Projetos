from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from rolepermissions.decorators import has_permission_decorator

from .models import Users


# Funções da tela cadastrar_usuario.
@has_permission_decorator('cadastrar_usuario')  # permite passar como parâmetro, a função ou o cargo.
def cadastrar_usuario(request):

    if request.method == 'GET':
        
        vendedores = Users.objects.filter(cargo="V") #  Buscando todos os vendedores.         
        return render(request, 'cadastrar_usuario.html', {'vendedores': vendedores})

    #   Criando um novo vendedor.
    elif request.method == 'POST':

        #   Verificando se o vendedor ja existe no Bd.
        user = Users.objects.filter(email=request.POST.get('email'))

        if user.exists():

            # TODO: Utilizar messagens do DJANGO.
            return HttpResponse('O Usuário já existe')

        #   Cadastrando novo vendedor.
        Users.objects.create_user(
            # Registrando nome do Usuário.
            username=request.POST.get('email'),
            # Registrando email do Usuário.
            email=request.POST.get('email'),
            # Registrando senha do Usuário.
            password=request.POST.get('senha'),
            # Verificando e inserindo o tipo de cargo.
            cargo= "V" if request.POST.get('cargo').upper() == 'VENDEDOR' else "G" if request.POST.get('cargo').upper() == 'GERENTE' else 0)

        # TODO: Redirecionar com uma mensagem.
        return HttpResponse('Usuário cadastrado.')


# Funções da tela de Login.
def login(request):
    if request.method == 'GET':

        if request.user.is_authenticated:  # Se o usuário estiver autenticado, redireciona para a tela de login.
            return redirect(reverse('login'))

        return render(request, 'login.html')

    elif request.method == 'POST':  # Realizando Login.

        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            # TODO: Redirecionar com mensagem de erro.
            return HttpResponse('Usuário Inválido')

        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')


def logout(request):
    request.session.flush()
    return redirect(reverse('login'))

# Funções da tela cadastrar_usuario.
def excluir_usuario(request, id): # Botão Excluir.
    
    return HttpResponse(id)

