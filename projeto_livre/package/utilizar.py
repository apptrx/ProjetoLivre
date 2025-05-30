import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_dados(caminho_relativo):
    caminho = os.path.join(BASE_DIR, caminho_relativo)
    if not os.path.exists(caminho):
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump({"usuarios": [], "livros": []}, f, indent=4, ensure_ascii=False)
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(caminho_relativo, dados):
    caminho = os.path.join(BASE_DIR, caminho_relativo)
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    