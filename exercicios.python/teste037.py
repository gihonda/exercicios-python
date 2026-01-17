num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversao: 
      [1]Binario
      [2]Octal
      [3]Hexadecimal''')
opcao = int(input("Opcao: "))
if opcao == 1:
    print(f"O numero {num} convertido em BINARIO e {bin(num)[2:]}")
elif opcao == 2:
    print(f"O numero {num} convetido em OCTAL e {oct(num)[2:]}")
elif opcao == 3:
    print(f"O numero {num} convertido em HEXADECIMAL e {hex(num)[2:]}")
else:
    print("Opcao invalida! Tente novamente!")