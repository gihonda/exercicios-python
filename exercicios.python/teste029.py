km = int(input("Quantos Km/h vc esta dirigindo? "))
limite = 80
if km <= limite:
    print("Tenha uma boa viagem!")
else:
    multa = (km - limite) * 7
    print(f"Cuidado! Vc esta {km - limite}Km acima da velocidade permitida e tera que pagar uma multa de R${multa}!")