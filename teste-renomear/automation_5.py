val1 = int(input("Digite um valor:"))
val2 = int(input("Digite outro valor:"))
print("1-Soma")
print ("2-Subtracao")
print("3-Multiplicacao")
print("4-Divisao")
opcao = int(input("Escolha uma das opcoes:"))

if opcao == 1:
    resultado = val1 + val2
elif opcao == 2:
    resultado = val1 - val2
elif opcao == 3:
    resultado = val1 * val2
elif opcao == 4:
    if val2 == 0:
        print("Erro: divisao por zero.")
        exit()
    else:
        resultado = val1 / val2
else:
    print("Opcao invalida")

print(f"O resultado e {resultado}")