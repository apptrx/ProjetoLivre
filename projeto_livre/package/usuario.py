import uuid
from utilizar import carregar_dados, salvar_dados
from main import dados, usuarios

class usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        self.id_usuario = str(uuid.uuid4())

    def autenticar(self):      
        login = 0
        for i in usuarios: #vem do banco de dados
            # Verifica se o nome e a senha estão corretos
            if i.nome == self.nome and i.senha == self.senha:
                print(f"Login bem-sucedido para o usuário {self.nome}")
                login = 1
                return True
        if login == 0:
            print("Nome de usuário ou senha incorretos.")
            return False
        
    def volta_objeto(self):
        return {
            "nome": self.nome,
            "senha": self.senha,
            "id_usuario": self.id_usuario
        }
    
    @staticmethod
    def trans_objeto(dados):
        return usuario(
            nome=dados["nome"],
            senha=dados["senha"]
        )
                
    def realizar_emprestimo(emprestimo):
        pass
    def realizar_devolucao(livro):
        pass