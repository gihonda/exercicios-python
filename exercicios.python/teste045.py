from random import randint
from time import sleep
itens = ["Pedra", "Papel", "Tesoura"]
computador = randint(0,2)
print('''Suas opcoes:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input("Qual e a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("="*20)
print(f"Computador escolheu {itens[computador]}")
print(f"Jogador escolheu {itens[jogador]}")
print("="*20)

if computador == 0:# computador jogou PEDRA
    if jogador == 0:
        print("EMPATOU!")
    elif jogador == 1:
        print("JOGADOR VENCEU!")
    elif jogador == 2:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1:# computador jogou PAPEL
    if jogador == 0:
     print("COMPUTADOR VENCEU!")
    elif jogador == 1:
        print("EMPATOU!")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2:# computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU!")
    elif jogador == 1:
        print("COMPUTADOR VENCEU!")
    elif jogador == 2:
        print("EMPATOU")
    else:
        print("JOGADA INVALIDA!")
        