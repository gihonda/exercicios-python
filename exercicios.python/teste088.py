from random import randint
lista = []
quant = int(input("Quantos jogos vc quer queu sorteie? "))
cont = 0
print("-=" * 30)
print("JOGO  MEGA SENA".center(40))
print("-=" * 30)
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
print(lista)