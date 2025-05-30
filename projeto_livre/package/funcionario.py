from package.usuario import Usuario
from package.livro import Livro
from package.utilizar import carregar_dados, salvar_dados
from package.mixin import LoggerMixin

dados = carregar_dados('dados/biblioteca.json')

class Funcionario(Usuario, LoggerMixin):
    def __init__(self, nome, senha, id_usuario=None):
        super().__init__(nome, senha, id_usuario, tipo="funcionario")

    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro = Livro(titulo, autor, ano)
        dados.setdefault("livros", []).append(novo_livro.volta_objeto())
        salvar_dados('dados/biblioteca.json', dados)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
        