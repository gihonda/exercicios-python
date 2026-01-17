print("="*40)
print("10 TERMOS DE UMA PA".center(40))
print("="*40)
termo = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = termo + (10-1) * razao
for i in range(termo,decimo + razao,razao):
    print(i, end=" -> ")
print("Acabou!")