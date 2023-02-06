from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from rolepermissions.decorators import has_permission_decorator

from .models import Users

# Funções da tela cadastrar_vendedor.
@has_permission_decorator('cadastrar_vendedor') # permite passar como parâmetro, a função ou o cargo.
def cadastrar_vendedor(request):
    
    if request.method == 'GET':
        
        return render(request, 'cadastrar_vendedor.html')
    
    #   Criando um novo vendedor.
    elif request.method == 'POST':
        
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cargo = request.POST.get('cargo')
        
        #   Verificando se o vendedor ja existe no Bd.
        user = Users.objects.filter(email=email)
        
        if user.exists():
            
            # TODO: Utilizar messagens do DJANGO.
            return HttpResponse('O Usuário já existe')
        
        #   Cadastrando novo vendedor.
        user = Users.objects.create_user(
            username=email, 
            email=email, 
            password=senha, 
            cargo= "V")
        
        # TODO: Redirecionar com uma mensagem.
        return HttpResponse('Usuário cadastrado.')

# Funções da tela de Login.
def login(request):
    
    if request.method == 'GET':
        
        if request.user.is_authenticated: #   Se o usuário estiver autenticado, redireciona para a tela de login.
            return redirect(reverse('login'))
            
        return render(request, 'login.html')
    
    elif request.method == 'POST': # Realizando Login.
        
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)
        
        if not user:
            #TODO: Redirecionar com mensagem de erro.
            return HttpResponse('Usuário Inválido')
        
        auth.login(request, user)
        return HttpResponse('Usuário logado com sucesso')

def logout(request):
    
    request.session.flush()
    return redirect(reverse('login'))