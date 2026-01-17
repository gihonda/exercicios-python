print("="*40)
print("10 TEMOS DE UMA PA".center(40))
print("="*40)
primeiro = int(input("Primeiro termo: "))
razao = int(input("razao: "))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f"{termo} -> ",end="")
        termo += razao
        c += 1
    print("PAUSA")
    mais = int(input("Quantos termos vc quer mostrar a mais? "))
print(f"Progressao finalizada com {total} termos mostrados")