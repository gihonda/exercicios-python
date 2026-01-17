from random import randint
computador = randint(0,10)
palpite = 0
acertou = False
print("Acabei de pensar em numero de 0 a 10.\nSera que vc consegue advinhar qual foi?")
while not acertou:
    jogador = int(input("Qual e o seu palpite? "))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais uma vez.")
        elif jogador > computador:
            print("Menos...Tente mais uma vez.")
print(f"Acertou com {palpite} tentativas. Parabens! ")
