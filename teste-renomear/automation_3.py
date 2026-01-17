lista = []
print("="*15)
print("LISTA DE COMPRA")
print("="*15)

while True:
    produto = str(input("Produto:"))
    if produto == "fim":
        break
    else:
        lista.append(produto)

print("="*15)
print("\n".join(lista))
print("="*15)