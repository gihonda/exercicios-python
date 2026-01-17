soma = 0
cont = 0
for num in range(1,501):
    if num % 2 != 0:
        if num % 3 == 0:
            soma = soma + num
            cont = cont + 1
print(f"A soma de todos os {cont} numeros e {soma}")
