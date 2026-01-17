preco = float(input("Qual é o preço do produto? "))
desconto = preco * 5 / 100
novopreco = preco - desconto
print(f"O produto que custava R${preco:.2f}, na promoção de 5% vai custar R${novopreco:.2f}.")
