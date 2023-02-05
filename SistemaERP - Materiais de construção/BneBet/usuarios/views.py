from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import render


@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    return HttpResponse('Teste')

# Create your views here.
