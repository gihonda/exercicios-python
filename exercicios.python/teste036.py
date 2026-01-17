casa = float(input("Qual o valor da casa? R$"))
sal = float(input("Qual o salario? R$"))
anos = float(input("Quantos anos? "))
pm = casa / (anos * 12)
print(f"Para pagar uma casa de R${casa} em {anos} anos a prestacao sera de R${pm:.2f}")
if pm > 30 / 100 * sal:
    print("Emprestimo NEGADO!")
else:
    print("Emprestimo CONCEDIDO!")