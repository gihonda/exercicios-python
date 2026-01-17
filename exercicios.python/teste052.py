num = int(input("Digite um numero: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m',c,end="")
        tot += 1
    else:
        print('\033[31m',c,end="")
print(f"\n\033[mO numero {num} foi dividido {tot} vezes! ")
if tot == 2:
    print("E portanto, e PRIMO!")
else:
    print("E portanto, NAO E PRIMO!")
    