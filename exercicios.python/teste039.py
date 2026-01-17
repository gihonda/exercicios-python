from datetime import date
hoje = date.today().year
ano = int(input("Qual seu ano de nascimento? "))
idade = hoje - ano
print(f"Quem nasceu em {ano} tem {idade} anos em {hoje}")
if idade < 18:
    prazo = 18 - idade
    print(f"Ainda faltam {prazo} anos para o alistamento")
    print(f"Seu alistamento sera em {hoje + prazo}")
elif idade > 18:
    prazo = idade - 18
    print(f"Vc ja deveria ter se alistado ha {prazo} anos.")
    print(f"Seu alistamento foi em {hoje - prazo}")
else:
    print(f"Vc tem que se alistar IMEDIATAMENTE!")
