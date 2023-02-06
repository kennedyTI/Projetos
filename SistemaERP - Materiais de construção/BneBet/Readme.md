Tutoriais:

	1ª) Ambiente virtual.
		
		1.1ª)python3 -m venv env => cria um ambiente virtual:
		
		1.2ª)env\Scripts\activate.bat => ativa o ambiente virtual:
		
		1.3ª) Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process => Execute esse código no PowerShell, Caso o env esteja bloqueado:
	
	2ª) Pip.
		
		2.1ª)python -m pip list => exibirá todos os pacotes instalados no ambiente virtual:
		
		2.2ª)pip freeze > requirements.txt => produzirá uma lista dos pacotes instalados:
		
		2.3ª)python -m pip install -r requirements.txt => instala todos os pacotes listados no requirements:

		2.4ª)pip uninstall NomeDaBiblioteca => Desinstala a biblioteca desejada.

	3ª) Django

		3.1ª)django-admin startproject NomeDoProjeto . => cria um novo projeto:

		3.2ª)python manage.py runserver => inicia o projeto:

		3.3ª)python3 manage.py startapp NomeDoApp=> cria um novo App(tela):

		3.4ª)python3 manage.py makemigrations => AINDA NÃO SEI PRA QUE SERVE.

		3.5ª)python manage.py migrate => AINDA NÃO SEI PRA QUE SERVE.

		3.6ª)python manage.py createsuperuser => Criar super usuário para o servidor.


****************OBJETIVOS****************
- Autenticação com níveis de acesso
- Docker*

-> Gerente
	- Cadastrar produtos
	- Liberar descontos
	- Estornar a venda
	- Cadastrar cliente
	- Realizar uma venda
	- Emitir relatórios
	- Realizar orçamento
	- Criar etiqueta do produto
	- Liberar crédito
	- Aceitar devolução

-> Vendedor
	- Cadastrar Cliente
	- Realizar venda
	- Consultar Estoque
	- Sinalizar para o gerente
	- Ver comissões
	- Realizar um orçamento

-> Caixa
	- Abrir caixa
	- Fechar caixa
	- Finalizar Compra
	- Fluxo de caixa

Extrair o requeriments


