import uuid
from utilizar import carregar_dados, salvar_dados
class Livro:
    def __init__(self, titulo, autor, ano, id_livro=None, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.id_livro = id_livro if id_livro else str(uuid.uuid4())
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Livro '{self.titulo}' emprestado com sucesso.")
        else:
            print(f"Livro '{self.titulo}' não está disponível para empréstimo.")
    

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Livro '{self.titulo}' devolvido com sucesso.")
        else:
            print(f"Livro '{self.titulo}' já está disponível.")

    def volta_objeto(self):
        return {
            "id_livro": self.id_livro,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano,
            "disponivel": self.disponivel
        }

    @staticmethod
    def trans_objeto(dados):
        return Livro(
            dados["titulo"],
            dados["autor"],
            dados["ano"],
            dados["id_livro"],
            dados.get("disponivel", True)
        )