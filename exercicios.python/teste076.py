lista = ("Lapis", 1.75, "Boracha", 0.50, "Caderno", 39.99, "Marca texto", 2.65, "Mochila", 199,
         "Regua", 2, "Tesoura", 3.75, "Cola", 2.99, "Fita adesiva", 1, "Post it", 4.50)
print("-"*40)
print("LISTAGEM DE PRECOS".center(40))
print("-"*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end="")
    else:
        print(f"R${lista[pos]:>7.2f}")
print("-"*40)