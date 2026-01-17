print("="*40)
print("10 TEMOS DE UMA PA".center(40))
print("="*40)
primeiro = int(input("Primeiro termo: "))
razao = int(input("razao: "))
termo = primeiro
c = 1
while c <= 10:
    print(f"{termo} -> ",end="")
    termo += razao
    c += 1
print("FIM")