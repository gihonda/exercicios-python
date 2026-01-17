from random import randint
print("-=" * 30)
print("VAMOS JOGAR PAR OU IMPAR".center(60))
print("-=" * 30)
soma = c = vitoria = 0
vencedor = ""
while True:
    jogador = int(input("Digite um valor: "))
    opcao = str(input("[P/I]? ")).strip().upper()[0]
    print("-" * 50)
    computador = randint(0,11)
    soma = jogador + computador
    if soma % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"
    print(f"Vc jogou {jogador} e o computador jogou {computador}. Total de {soma} deu {resultado}")
    print("-" * 60)
    if opcao == "P":
        if soma % 2 == 0:
            print("Vc VENCEU!")
            c += 1
        else:
            print("Vc PERDEU!")
            break
    elif opcao == "I":
        if soma % 2 != 0:
            print("Vc VENCEU!")
            c += 1
        else:
            print("Vc PERDEU!")
            break
    print("Vamos jogar novamente...")
    print("-" * 60)
print("-=" * 30)
print(f"GAME OVER! Vc venceu {c} vezes.")
print("FIM")
