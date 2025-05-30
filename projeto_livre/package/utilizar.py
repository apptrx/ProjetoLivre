import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Funções para carregar e salvar dados em JSON

def carregar_dados(caminho_relativo):
    caminho = os.path.join(BASE_DIR, caminho_relativo)
    if not os.path.exists(caminho):
        with open(caminho, 'w') as f:
            json.dump({"usuarios": [], "livros": []}, f, indent=4)
    with open(caminho, 'r') as f:
        return json.load(f)

def salvar_dados(caminho_relativo, dados):
    caminho = os.path.join(BASE_DIR, caminho_relativo)
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    