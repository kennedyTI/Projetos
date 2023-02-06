from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_vendedor') # permite passar como parâmetro, a função ou o cargo.
def cadastrar_vendedor(request):
    return render(request, 'cadastrar_vendedor.html')