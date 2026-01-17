num = int(input("Digite um número pra ver sua tabuada:"))
for i in range(1,11):
    print(f"{num:>2} X {i:>2} = {num * i:>4}")
