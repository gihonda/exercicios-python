n = (int(input("Digite um valor: ")), 
     int(input("Digite um outro valor: ")), 
     int(input("Digite mais um valor: ")), 
     int(input("Digite o ultimo valor: ")))
print(f"O numero 9 apareceu {n.count(9)} vezes. ")
if 3 in n:
    print(f"O primeiro valor 3 foi digitado na posicao {n.index(3)+1}. ")
else:
    print("O valor 3 nao foi digitado. ")
print("Os valores pares digitados foram ", end='')
for c in n:
    if c % 2 == 0:
        par = c
        print(f"{par}", end= ' ')
