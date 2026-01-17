print("Calculadora simples")
n1 = int(input("Digite um número:"))
operador = str(input("Escolha um operador(+, -, *, /):"))
n2 = int(input("Digite outro número:"))

if operador == "+":
    resultado = n1 + n2
elif operador == '-':
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Erro: divisão por zero!"
else:
    resultado = "Operador inválido!"
print("Resultado:", resultado)