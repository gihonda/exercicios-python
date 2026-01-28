from random import sample
from time import sleep
jogos = []
print("-=" * 20)
print("JOGO DA MEGA SENA".center(40))
print("-=" * 20)
print()
quant = int(input("Quantos jogos vc quer que eu sorteie? "))
print()
print("-=" * 5, f"SORTEANDO {quant} JOGOS", "-=" * 5)
print()
for n in range(quant):
    jogos.append(sample(range(1, 61), 6))
    jogos[n].sort()
    print(f"jogo {n + 1}: {jogos[n]}") 
    sleep(1)
print()
print("-=" * 5, "<BOA SORTE!>", "-=" * 5)
