from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from rolepermissions.decorators import has_permission_decorator

#   Nosso Código
from .models import Users


# Funções da tela cadastrar_usuario.

@has_permission_decorator('usuario')  # permite passar como parâmetro, a função ou o cargo.
def cadastrar_usuario(request):
    if request.method == 'GET':

        return render(
            request,
            'cadastrar_usuario.html',
            {
                'usuarios': Users.objects.all()  # Buscando todos os usuários.
            }
        )

    #   Criando um usuario.
    elif request.method == 'POST':

        #   Verificando se o vendedor ja existe no Bd.
        #user = Users.objects.filter(email=request.POST.get('email'))

        if Users.objects.filter(email=request.POST.get('email')).exists():
            # TODO: Utilizar messagens do DJANGO.
            return HttpResponse('O Usuário já existe')

        #   Verificando se a senha está coincidindo.
        if not request.POST.get('senha') == request.POST.get('confirmarSenha'):
            # TODO: Redirecionar com uma mensagem.
            return HttpResponse('As senhas não coincidem.')

        #   Cadastrando novo usuário.
        Users.objects.create_user(
            username=request.POST.get('email'),  # Registrando Login do Usuário.
            first_name=request.POST.get('nome'),  # Registrando Nome do Usuário.
            last_name=request.POST.get('sobrenome'),  # Registrando Sobrenome do Usuário.
            email=request.POST.get('email'),  # Registrando email do Usuário.
            password=request.POST.get('senha'),  # Registrando senha do Usuário.
            cargo="V" if request.POST.get('cargo').upper() == 'VENDEDOR' else "G" if request.POST.get(
                'cargo').upper() == 'GERENTE' else 0,  # Verificando e inserindo o tipo de cargo.
        )

        # TODO: Redirecionar com uma mensagem.
        return redirect(reverse('cadastrar_usuario'))


@has_permission_decorator('usuario')  # permite passar como parâmetro, a função ou o cargo.
def excluir_usuario(request, id):  # Botão Excluir.

    # Buscando um dado dentro da tabela Users.
    usuario = get_object_or_404(
        Users,
        id=id
    )
    usuario.delete()

    # Excluindo o usuário.
    messages.add_message(
        request,
        messages.SUCCESS,
        'Usuário excluido com sucesso!'
    )
    return redirect(reverse('cadastrar_usuario'))
