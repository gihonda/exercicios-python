valores = [[], []]
for v in range(0,7):
    n = int(input(f"Digite um valor: "))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print("-=" *30)
print(f"Os valores pares digitados foram {sorted(valores[0])}")
print(f"Os valores impares digitados foram {sorted(valores[1])}")
