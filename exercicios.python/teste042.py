print("="* 40)
print("ANALIZADOR DE TRIANGULOS".center(40))
print("="* 40)
s1 = int(input("Primeiro Segmento: "))
s2 = int(input("segundo segmento: "))
s3 = int(input("Terceiro segmento: "))
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print("Esses segmentos PODEM FORMAR  um triangulo ", end='')
    if s1 == s2 == s3:
        print("EQUILATERO")
    elif s1 != s2 != s3 != s1:
        print("ESCALENO")
    else:
        print("ISOCELES")
else:
    print("Esses segmentos NAO PODEM FORMAR um triangulo.")
