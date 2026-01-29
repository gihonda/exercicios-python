nome = str(input("Nome do funcionario: "))
anos = int(input("Ano de nascimento: "))
ctps = int(input("Carteira de trabalho (0 se nao tem): "))
idade = 2026 - anos
funcionario = {"nome": nome, "idade": idade, "ctps": ctps}
if ctps != 0:
    contratacao = int(input("Ano de contratacao: "))
    salario = float(input("Salario: R$"))
    aposentadoria = (contratacao + 35) - anos
    funcionario["contratacao"] = contratacao
    funcionario["salario"] = salario
    funcionario["aposentadoria"] = aposentadoria
print("-=" * 30)
for k, v in funcionario.items():
    print(f"  -{k} tem o valor {v}")
    