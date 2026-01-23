lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    resp = str(input("Quer continuar? [S?N]: ")).strip().upper()
    if resp not in "SN":
        print("Resposta invalida! Tente novamente.")
    elif resp in "N":
        break

print("-="*30)
print(f"Foram digitados {len(lista)} elementos...")
lista.sort(reverse = True)
print(f"Os valores em ordem decrescente sao {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 nao foi encontrado na lista!")
    