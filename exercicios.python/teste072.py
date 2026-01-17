extenso = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input("Digite um numero:"))
    if num <= 20:
        print(f"Vc digitou o numero {extenso[num]}")
        break
    else:
        print("Tente novamente.", end= "")
print("-" *30)