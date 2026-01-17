print("="*50)
print("ANALIZADOR DE TRIANGULOS".center(50))
print("="*50)
r1 = int(input("Primeiro segmento: "))
r2 = int(input("Segundo segmento:  "))
r3 = int(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Esses segmentos FORMAM UM TRIANGULO!")
else:
    print("Esses segmentos NAO FORMAM UM TRIANGULO!")