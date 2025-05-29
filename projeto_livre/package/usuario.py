import uuid
from utilizar import carregar_dados, salvar_dados
from main import dados, usuarios

class Usuario:
    def __init__(self, nome, senha, id_usuario=None, tipo='comum'):
        self.nome = nome
        self.senha = senha
        self.id_usuario = id_usuario if id_usuario else str(uuid.uuid4())
        self.tipo = tipo
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
            "id_usuario": self.id_usuario,
            "tipo": self.tipo
        }
    
    @staticmethod
    def trans_objeto(dados):
        return Usuario(
            dados["nome"],
            dados["senha"],
            dados["id_usuario"],
            dados.get("tipo", "comum")
        )
                
    def realizar_emprestimo(emprestimo):
        pass
    def realizar_devolucao(livro):
        pass