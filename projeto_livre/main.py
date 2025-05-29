from package.usuario import usuario
from dados import biblioteca
from package.utilizar import carregar_dados 

dados = carregar_dados('dados/biblioteca.json')
usuarios = [usuario.trans_objeto(d) for d in dados['usuarios']]

print("Bem-vindo ao sistema de gerenciamento de usuários!")
escolha = input("Por favor, fará o login ou registro? ")
if escolha.lower() == 'registro':
    nome_input = input("Digite seu nome de usuário: ")
    senha_input = input("Digite sua senha: ")
    novo_usuario = usuario(nome_input, senha_input)
    usuarios.append(novo_usuario)
    dados['usuarios'].append(novo_usuario.volta_objeto())
elif escolha.lower() == 'login':
    nome_input = input("Usuário: ")
    senha_input = input("Senha: ")
    usuario = usuario(nome_input, senha_input)
    if usuario.autenticar():
        print("Login realizado com sucesso!")
    else:
        print("Falha no login. Verifique seu nome de usuário e senha.")
