import os
caminho = "teste-renomear"
print("Arquivos encontrados na pasta 'teste-renomear': ")
arquivos = os.listdir(caminho)
print(arquivos)

contador = 1
for nome in arquivos:
    if nome.endswith(".py"):
        novo_nome = f"automation_{contador}.py"
        caminho_antigo = os.path.join(caminho, nome)
        caminho_novo = os.path.join(caminho, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f"{nome} -> {novo_nome}")
        contador += 1