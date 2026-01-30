print("=" * 40)
print("10 TERMOS DE UMA PA".center(40))
print("=" * 40)
primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    cont += 1
print(">>> FIM <<<")