print("LOJA OLIVEIRA".center(80,'='))
preco = float(input("Preco das compras: R$"))
print('''FORMAS DE PAGAMENTO
      [ 1 ] a vista dinheiro/PIX
      [ 2 ] a vista cartao
      [ 3 ] 2x no cartao
      [ 4 ] 3x ou mais no cartao''')
opcao = int(input("Qual e a opcao? "))
if opcao == 1:
    novopreco = preco - (preco * 10 / 100)
    print(f"Sua compra de R${preco} vai custar R${novopreco:.2f} no final.")
elif opcao == 2:
    novopreco = preco - (preco * 5 / 100)
    print(f"Sua compra de R${preco} vai custar R${novopreco:.2f} no final")
elif opcao == 3:
    print(f"Sua compra de R${preco} vai ficar em 2x R${preco / 2:.2f}")
elif opcao == 4:
    novopreco = preco + (preco * 20 / 100)
    totparc = int(input("Em quantas parcelas? "))
    parcela = novopreco / totparc
    print(f"Sua compra vai ficar em {totparc} parcelas de R${novopreco / totparc}")
    print(f"Sua compra de {preco} vai ficar R${novopreco} no final.")
else:
    print("Opcao invalida. Tente novamente.")