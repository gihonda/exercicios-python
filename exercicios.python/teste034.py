sal = float(input("Qual e o seu salario? R$"))
if sal <= 1250:
    aumento = sal + (sal * 10 / 100)
else:
    aumento = sal + (sal * 15 / 100)
print(f"Quem ganhava R${sal:.2f} vai passar a ganhar R${aumento:.2f}")