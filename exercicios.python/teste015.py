dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
preco = (60*dias) + (0.15*km)
print(f"O total a pagar e R${preco:.2f}")