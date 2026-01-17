c = 0
soma = 0
n = 0
while n != 999:
    n = int(input("Digite um numero [999 para parar]: "))
    if n != 999:
        soma = soma + n
        c += 1
print(f"Vc digitou {c} numeros e a soma foi {soma}.")
