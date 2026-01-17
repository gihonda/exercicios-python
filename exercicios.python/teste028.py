from random import randint
from time import sleep
n = randint(0,5)
print("-=-"*20)
print("Vou pensar em um numero de 0 a 5...")
print("-=-"*20)
sleep(3)
escolha = int(input("Tente adivinhar..."))
if escolha == n:
    print("Parabens! Vc acertou!")
else:
    print("Errou! Tente novamente.")