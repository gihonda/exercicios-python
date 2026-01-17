from datetime import date
hoje = date.today().year
ano = int(input("Qual o ano de nascimento? "))
idade = hoje - ano
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Classificacao: MIRIM")
elif idade <= 14:
    print("Classificacao: INFANTIL")
elif idade <= 19:
    print("Classificacao: JUNIOR")
elif idade <= 25:
    print("Classificacao: SENIOR")
else:
    print("Classificacao: MASTER")
