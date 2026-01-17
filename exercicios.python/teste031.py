viagem = int(input("Qual e a distancia da sua viagem? "))
if viagem > 200:
    preco = viagem * 0.45
else:
    preco = viagem * 0.50
print(f"Sua viagem e de {viagem}Km e vai custar R${preco:.2f}")