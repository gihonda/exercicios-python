soma = 0
cont = 0
for num in range(1,7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f"Vc digitou {cont} numeros pares e asoma foi {soma}")