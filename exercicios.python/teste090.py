aluno = {"nome": "", "media": 0, "situacao": ""}
aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Media de {aluno["nome"]}: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"
print("-=" * 25)
print(f"Nome:{aluno['nome']}")
print(f"Media: {aluno['media']}")
print(f"Situacao: {aluno['situacao']}")
