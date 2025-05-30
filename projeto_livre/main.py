from package.usuario import Usuario
import dados 
from package.utilizar import carregar_dados, salvar_dados 
from package.funcionario import Funcionario

dados = carregar_dados('dados/biblioteca.json')
# Carrega dados do JSON

usuarios = [usuario.trans_objeto(d) for d in dados['usuarios']]
# Converte dicionário em objeto 

print("Bem-vindo ao sistema de gerenciamento de usuários!")
escolha = input("Por favor, digite 'login' ou 'registro: ")
if escolha.lower() == 'registro':
    nome_input = input("Digite seu nome de usuário: ")
    senha_input = input("Digite sua senha: ")
    novo_usuario = Usuario(nome_input, senha_input)
    usuarios.append(novo_usuario)
    dados['usuarios'].append(novo_usuario.volta_objeto())
    salvar_dados('dados/biblioteca.json', dados)
    print("Usuário criado com sucesso!")
elif escolha.lower() == 'login':
    nome_input = input("Usuário: ")
    senha_input = input("Senha: ")
    usuario = Usuario(nome_input, senha_input)
    
    if usuario.autenticar(usuarios):
        print("Login realizado com sucesso!")
        if usuario.tipo == "funcionario":
            print("Bem-vindo, funcionário!")
            funcionario = Funcionario(nome_input, senha_input)
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            funcionario.cadastrar_livro(titulo, autor, ano)
        else:
            print("Bem-vindo, usuário comum!")
    else:
        print("Falha no login. Verifique seu nome de usuário e senha.")
else:
    print("Opção inválida. Por favor, escolha 'login' ou 'registro'.")
