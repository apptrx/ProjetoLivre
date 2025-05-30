from package.usuario import Usuario
from package.utilizar import carregar_dados, salvar_dados 
from package.funcionario import Funcionario
from package.livro import Livro
from package.emprestimo import Emprestimo  

livros = [Livro.trans_objeto(l) for l in carregar_dados('dados/biblioteca.json')['livros']]

dados = carregar_dados('dados/biblioteca.json')
# Carrega dados do JSON

usuarios = [Usuario.trans_objeto(d) for d in dados['usuarios']]
# Converte dicionário em objeto 


print("Bem-vindo ao sistema de gerenciamento de usuários!")
escolha = ''
while escolha.lower() not in ['login', 'registro']:
    escolha = input("Por favor, digite 'login' ou 'registro': ").strip().lower()
    if escolha not in ['login', 'registro']:
        print("Opção inválida. Tente novamente.")

if escolha == 'registro':
    nome_input = input("Digite seu nome de usuário: ")
    senha_input = input("Digite sua senha: ")
    tipo = input("Digite o tipo de usuário (comum/funcionario): ").lower()

    while tipo not in ['comum', 'funcionario']:
        tipo = input("Digite o tipo de usuário (comum/funcionario): ").lower() 

    novo_usuario = Usuario(nome_input, senha_input, tipo=tipo)
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
        else:
            print("Bem-vindo, usuário comum!")
    else:
        print("Falha no login. Verifique seu nome de usuário e senha.")
while True:
    print("\n --- MENU --- ")
    if usuario_logado.tipo == "funcionario":
        print("1. Cadastrar livro")
        print("2. ver livros disponíveis")
        print("3. Realizar empréstimo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            funcionario.cadastrar_livro(titulo, autor, ano)
        elif opcao == '2':
            for livro in livros:
                if livro.disponivel:
                    print(f"{livro.titulo} - {livro.autor} ({livro.ano})")
        elif opcao == '3':
            titulo = input("Digite o título do livro que deseja emprestar: ")
            livro_encontrado = next((livro for livro in livros if livro.titulo.lower() == titulo.lower() and livro.disponivel), None)
            if livro_encontrado:
                usuario_logado.realizar_emprestimo(Emprestimo(livro_encontrado, usuario_logado))
            else:
                print("Livro não encontrado ou indisponível.")
        elif opcao == '4':
            print("Obrigado por ter entrado na nossa biblioteca!")
            break
    elif usuario_logado.tipo == "comum":
        print("1. ver livros disponíveis")
        print("2. Realizar empréstimo")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            for livro in livros:
                if livro.disponivel:
                    print(f"{livro.titulo} - {livro.autor} ({livro.ano})")
        elif opcao == '2':
            titulo = input("Digite o título do livro que deseja emprestar: ")
            livro_encontrado = next((livro for livro in livros if livro.titulo.lower() == titulo.lower() and livro.disponivel), None)
            if livro_encontrado:
                usuario_logado.realizar_emprestimo(Emprestimo(livro_encontrado, usuario_logado))
            else:
                print("Livro não encontrado ou indisponível.")
        elif opcao == '3':
            print("Obrigado por ter entrado na nossa biblioteca!")
            break

