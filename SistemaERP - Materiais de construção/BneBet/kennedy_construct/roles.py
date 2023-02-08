from rolepermissions.roles import AbstractUserRole

'''
    Local para: 
        1ª) Criar Perfil.
        2ª) Adicionar permissões de cada tipo de perfil.
        
'''


class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'cadastrar_usuario': True,
        'liberar_descontos': True,
    }


class Vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True,
    }
