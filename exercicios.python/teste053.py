frase = str(input("Digite uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = junto[::-1]
print(f"O inverso de {junto} e {inverso}!")
if inverso == junto:
    print("Temos um PALIDROMO")
else:
    print("A frase digitada nao e um palidromo!")
