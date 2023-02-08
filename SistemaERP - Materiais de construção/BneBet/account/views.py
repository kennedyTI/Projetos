from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import render


# Funções da tela de Login.
def entrar(request):
    if request.method == 'GET':

        if request.user.is_authenticated:  # Se o usuário estiver autenticado, redireciona para a tela de login.
            return redirect(reverse('entrar'))

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


def sair(request):
    request.session.flush()
    return redirect(reverse('entrar'))
