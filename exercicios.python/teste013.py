salario = float(input("Qual e o salario do funcionario? R$"))
aumento = salario * 15 / 100
novosalario = salario + aumento
print(f"Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, vai passar a ganhar R${novosalario:.2f}")