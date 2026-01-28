from random import sample
from time import sleep
jogos = []
print("-=" * 20)
print("JOGO DA MEGA SENA".center(40))
print("-=" * 20)
quant = int(input("Quantos jogos vc quer que eu sorteie? "))
print()
for n in range(quant):
    jogos.append(sample(range(1, 61), 6))
    jogos[n].sort()
    print(f"Jogo {n + 1}: {jogos[n]}")
    sleep(1)
print("-=" * 3, f"FIM DO SORTEIO", "-=" * 3)
