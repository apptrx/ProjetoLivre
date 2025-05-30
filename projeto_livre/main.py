from package.usuario import Usuario
from package.utilizar import carregar_dados, salvar_dados
from package.funcionario import Funcionario
from package.livro import Livro
from package.emprestimo import Emprestimo
from datetime import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')

def carregar_tudo():
    dados = carregar_dados('dados/biblioteca.json')
    livros = [Livro.trans_objeto(l) for l in dados.get("livros", [])]
    usuarios = [Usuario.trans_objeto(u) for u in dados.get("usuarios", [])]
    return dados, livros, usuarios

def salvar_emprestimo(emprestimo, livro, dados):
    dados["emprestimos"] = dados.get("emprestimos", [])
    dados["emprestimos"].append(emprestimo.volta_objeto())
    for i, l in enumerate(dados["livros"]):
        if l["id_livro"] == livro.id_livro:
            dados["livros"][i] = livro.volta_objeto()
    salvar_dados("dados/biblioteca.json", dados)

def menu_usuario(usuario, livros, dados):
    while True:
        print("\n--- MENU USUÁRIO ---")
        print("1. Ver livros disponíveis")
        print("2. Realizar empréstimo")
        print("3. Devolver livro")
        print("4. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            for livro in livros:
                if livro.disponivel:
                    print(f"{livro.titulo} - {livro.autor} ({livro.ano})")

        elif opcao == '2':
            titulo = input("Título do livro: ")
            livro = next((l for l in livros if l.titulo.lower() == titulo.lower() and l.disponivel), None)
            if livro:
                emprestimo = Emprestimo(livro.id_livro, usuario.id_usuario)
                livro.disponivel = False
                salvar_emprestimo(emprestimo, livro, dados)
                print(f"Livro '{livro.titulo}' emprestado com sucesso.")
                dados, livros, _ = carregar_tudo()
            else:
                print("Livro não disponível.")

        elif opcao == '3':
            meus_emprestimos = [e for e in dados.get("emprestimos", []) if e["id_usuario"] == usuario.id_usuario and not e["data_devolucao"]]
            if not meus_emprestimos:
                print("Você não tem empréstimos ativos.")
                continue

            print("\nSeus empréstimos:")
            for idx, e in enumerate(meus_emprestimos):
                livro = next((l for l in livros if l.id_livro == e["id_livro"]), None)
                if livro:
                    print(f"{idx + 1}. {livro.titulo} - {livro.autor}")

            escolha = int(input("Número do livro para devolver: ")) - 1
            emprestimo = meus_emprestimos[escolha]
            emprestimo["data_devolucao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for l in livros:
                if l.id_livro == emprestimo["id_livro"]:
                    l.disponivel = True

            for i, e in enumerate(dados["emprestimos"]):
                if e["id_emprestimo"] == emprestimo["id_emprestimo"]:
                    dados["emprestimos"][i] = emprestimo

            for i, l in enumerate(dados["livros"]):
                if l["id_livro"] == emprestimo["id_livro"]:
                    dados["livros"][i] = next((livro.volta_objeto() for livro in livros if livro.id_livro == l["id_livro"]), l)

            salvar_dados("dados/biblioteca.json", dados)
            print("Livro devolvido com sucesso!")
            dados, livros, _ = carregar_tudo()

        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def menu_funcionario(funcionario, livros, dados):
    while True:
        print("\n--- MENU FUNCIONÁRIO ---")
        print("1. Cadastrar livro")
        print("2. Ver livros disponíveis")
        print("3. Realizar empréstimo")
        print("4. Devolver livro")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            funcionario.cadastrar_livro(titulo, autor, ano)
            dados, livros, _ = carregar_tudo()

        elif opcao == '2':
            for livro in livros:
                if livro.disponivel:
                    print(f"{livro.titulo} - {livro.autor} ({livro.ano})")

        elif opcao == '3':
            titulo = input("Título do livro: ")
            livro = next((l for l in livros if l.titulo.lower() == titulo.lower() and l.disponivel), None)
            if livro:
                emprestimo = Emprestimo(livro.id_livro, funcionario.id_usuario)
                livro.disponivel = False
                salvar_emprestimo(emprestimo, livro, dados)
                print(f"Livro '{livro.titulo}' emprestado com sucesso.")
                dados, livros, _ = carregar_tudo()
            else:
                print("Livro não disponível.")

        elif opcao == '4':
            meus_emprestimos = [e for e in dados.get("emprestimos", []) if e["id_usuario"] == funcionario.id_usuario and not e["data_devolucao"]]
            if not meus_emprestimos:
                print("Você não tem empréstimos ativos.")
                continue

            print("\nSeus empréstimos:")
            for idx, e in enumerate(meus_emprestimos):
                livro = next((l for l in livros if l.id_livro == e["id_livro"]), None)
                if livro:
                    print(f"{idx + 1}. {livro.titulo} - {livro.autor}")

            escolha = int(input("Número do livro para devolver: ")) - 1
            emprestimo = meus_emprestimos[escolha]
            emprestimo["data_devolucao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for l in livros:
                if l.id_livro == emprestimo["id_livro"]:
                    l.disponivel = True

            for i, e in enumerate(dados["emprestimos"]):
                if e["id_emprestimo"] == emprestimo["id_emprestimo"]:
                    dados["emprestimos"][i] = emprestimo

            for i, l in enumerate(dados["livros"]):
                if l["id_livro"] == emprestimo["id_livro"]:
                    dados["livros"][i] = next((livro.volta_objeto() for livro in livros if livro.id_livro == l["id_livro"]), l)

            salvar_dados("dados/biblioteca.json", dados)
            print("Livro devolvido com sucesso!")
            dados, livros, _ = carregar_tudo()

        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def main():
    dados, livros, usuarios = carregar_tudo()
    print("Bem-vindo à biblioteca!")

    escolha = ""
    while escolha not in ['login', 'registro']:
        escolha = input("Digite 'login' ou 'registro': ").lower()

    if escolha == 'registro':
        nome = input("Nome: ")
        senha = input("Senha: ")
        tipo = ""
        while tipo not in ['comum', 'funcionario']:
            tipo = input("Tipo (comum/funcionario): ").lower()
        novo_usuario = Usuario(nome, senha, tipo=tipo)
        usuarios.append(novo_usuario)
        dados["usuarios"].append(novo_usuario.volta_objeto())
        salvar_dados("dados/biblioteca.json", dados)
        dados, livros, usuarios = carregar_tudo()
        print("Usuário registrado.")
        if tipo == "funcionario":
            menu_funcionario(Funcionario(novo_usuario.nome, novo_usuario.senha, novo_usuario.id_usuario), livros, dados)
        else:
            menu_usuario(novo_usuario, livros, dados)

    elif escolha == 'login':
        nome = input("Nome: ")
        senha = input("Senha: ")
        temp = Usuario(nome, senha)
        logado = temp.autenticar(usuarios)
        if logado:
            print(f"Login como {logado.nome}")
            if logado.tipo == "funcionario":
                menu_funcionario(Funcionario(logado.nome, logado.senha, logado.id_usuario), livros, dados)
            else:
                menu_usuario(logado, livros, dados)
        else:
            print("Login falhou.")
            main()

if __name__ == "__main__":
    main()
