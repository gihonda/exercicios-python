maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input(f"Peso da {pess} pessoa: "))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
                menor = peso
print(f"O maior peso lido foi {maior}Kg.\nO menor peso lido foi {menor}Kg.")