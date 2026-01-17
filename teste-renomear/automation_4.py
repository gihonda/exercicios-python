import os
caminho = "teste-renomear"
print("Arquivos da subpasta'teste-renomear':")
arquivo = os.listdir(caminho)
for nome in arquivo:
    if nome.endswith(".py"):
        caminho_completo = os.path.join(caminho, nome)
        print(f"Caminho completo: {caminho_completo}")
