from datetime import datetime
import uuid

class Emprestimo:
    def __init__(self, id_livro, id_usuario, data_emprestimo=None, data_devolucao=None, id_emprestimo=None):
        self.id_emprestimo = id_emprestimo if id_emprestimo else str(uuid.uuid4())
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo if data_emprestimo else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_devolucao = data_devolucao

    def devolver(self):
        self.data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def volta_objeto(self):
        return {
            "id_emprestimo": self.id_emprestimo,
            "id_livro": self.id_livro,
            "id_usuario": self.id_usuario,
            "data_emprestimo": self.data_emprestimo,
            "data_devolucao": self.data_devolucao
        }
    
    @staticmethod
    def trans_objeto(dados):
        return Emprestimo(
            dados["id_livro"],
            dados["id_usuario"],
            dados["data_emprestimo"],
            dados["data_devolucao"],
            dados["id_emprestimo"],
        )