from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input(">>>>> Qual e a sua opcao? "))
    if opcao == 1:
        print(f"A soma entre {n1} e {n2} e {n1+n2}")
    elif opcao == 2:
        print(f"O resultado de {n1} x {n2} e {n1*n2}")
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else: maior = n2
        print(f"Entre {n1} e {n2} o maior e {maior} ")
    elif opcao == 4:
        print("Informe os valores novamente:")
        n1 = int(input("Primeiro valor:"))
        n2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Finalizando...")
        sleep(2)
    else:
        print("Opcao invalida. Tente novamente.")
    print("-="* 10)
print("Fim de pograma. Volte sempre!")