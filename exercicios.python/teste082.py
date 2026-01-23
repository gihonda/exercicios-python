lista = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    resp = str(input("Quer continuar? [S?N]: ")).strip().upper()
    if resp not in "SN":
        print("Resposta invalida. Tente novamente.")
    elif resp in "N":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("=-"*30)
print(f"A lista completa e {lista}")
print(f"A lista de pares e {pares}")
print(F"A lista de impares e {impares}")
