from package.usuario import Usuario
from package.utilizar import carregar_dados, salvar_dados 
from package.funcionario import Funcionario

dados = carregar_dados('dados/biblioteca.json')
# Carrega dados do JSON

usuarios = [Usuario.trans_objeto(d) for d in dados['usuarios']]
# Converte dicionário em objeto 

print("Bem-vindo ao sistema de gerenciamento de usuários!")
escolha = ''
while escolha.lower() not in ['login', 'registro']:
    escolha = input("Por favor, digite 'login' ou 'registro: ").strip().lower()
    if escolha not in ['login', 'registro']:
        print("Opção inválida. Tente novamente.")

if escolha == 'registro':
    nome_input = input("Digite seu nome de usuário: ")
    senha_input = input("Digite sua senha: ")
    tipo = input("Digite o tipo de usuário (comum/funcionario): ").lower()

    while tipo not in ['comum', 'funcionario']:
        tipo = input("Digite o tipo de usuário (comum/funcionario): ").lower() 

    novo_usuario = Usuario(nome_input, senha_input, tipo)
    usuarios.append(novo_usuario)
    dados['usuarios'].append(novo_usuario.volta_objeto())
    salvar_dados('dados/biblioteca.json', dados)
    print("Usuário criado com sucesso!")
else:
    nome_input = input("Usuário: ")
    senha_input = input("Senha: ")
    usuario = Usuario(nome_input, senha_input)
    usuario_logado = usuario.autenticar(usuarios)
    
    if usuario_logado:
        print(f"Login realizado: {usuario_logado.nome}")
        if usuario_logado.tipo == "funcionario":
            print("Bem-vindo, funcionário!")
            funcionario = Funcionario(usuario_logado.nome, usuario_logado.senha, usuario_logado.id_usuario)
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            funcionario.cadastrar_livro(titulo, autor, ano)
        else:
            print("Bem-vindo, usuário comum!")
    else:
        print("Falha no login. Verifique seu nome de usuário e senha.")
