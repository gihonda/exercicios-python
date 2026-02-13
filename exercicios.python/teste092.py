from datetime import datetime
funcionario = str(input("Nome do funcionario: "))
anonascimento = int(input("Ano de nascimento: "))
ctps = int(input("Carteira de trabalho (0 se nao tiver): "))
idade = datetime.now().year - anonascimento
cadastro = {"nome": funcionario, "idade": idade, "ctps": ctps}
if ctps != 0:
    ano_contratacao = int(input("Ano de contratacao: "))
    salario = float(input("Salario: R$"))
    cadastro["ano_contratacao"] = ano_contratacao
    cadastro["salario"] = salario
    cadastro["aposentadoria"] = ano_contratacao + 35 - anonascimento
print("-=" * 30)
for k, v in cadastro.items():
    print(f"  -{k} tem o valor {v}")
