lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor para a posicao {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
print(f"Vc digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} na posicao ",end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...",end='')
print()
print(f"O menor valor digitado foi {menor} na posicao ",end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...",end='')
