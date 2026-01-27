galera = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    continuar = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if continuar == "N":
        break
print("-=" *30)
print(f"Ao todo vc cadastrou {len(galera)} pessoas.")
print(f"O maior peso foi de {maior}kg.Peso de ", end="")
for p in galera:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}kg. Peso de ", end="")
for p in galera:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
