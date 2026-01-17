peso = float(input("Qual e o seu peso? "))
altura = int(input("Qual e a altura em cm? "))
imc = peso / ((altura / 100) ** 2)
print(f" Uma pessoa de {peso}Kg e {altura}cm tem o IMC  de {imc:.2f}")
if imc < 18.5:
    print("Vc esta ABAIXO do peso!")
elif imc < 25:
    print("Vc esta com peso IDEAL!")
elif imc < 30:
    print("Vc esta com SOBREPESO!")
elif imc < 40:
    print("Vc esta com OBESIDADE!")
else:
    print("OBESIDADE MORBIDA!")