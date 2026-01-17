print("-" * 40)
print("LOJA SUPER BARATÃO".center(40))
print("-" * 40)
total = tot1000 = menor = cont = 0
barato = ""
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preco: R$"))
    cont += 1
    total += preco
    if preco > 1000:
         tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp == "N":
        break
print("FIM DE PROGRAMA".center(40, "-"))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {tot1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custou R${menor:.2f}")
