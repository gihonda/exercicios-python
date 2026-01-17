resp = ""
soma = c = maior = menor = 0
while resp != "N":
    n = int(input("Digite um numero: "))
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp != "S" and resp != "N":
        print("Resposta invalida.")
    soma = soma + n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / c
print(f"Vc digitou {c} numeros e a media foi {media:.2f}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
