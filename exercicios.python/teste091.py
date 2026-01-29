from random import sample
from time import sleep
jogadores = {}
numeros = sample(range(1, 7), 4)
print("Valores sorteados:")
for i, n in enumerate(numeros, start=1):
    jogadores[f"Jogador {i}"] = n
for k, v in jogadores.items():
    print(f"{k} tirou {v} no dado. ")
    sleep(0.5)
print("==RANKING DOS JOGADORES==")
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse = True)
for i, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{i} lugar: {jogador} com {valor}.")
    sleep(0.5)
