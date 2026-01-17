nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Tirando {nota1:.2f} e {nota2:.2f}, a media do aluno sera {media:.2f}")
if media < 5.0:
    print("O aluno esta REPROVADO!")
elif media > 7.0:
    print("O aluno esta APROVADO!")
else:
    print("O aluno esta em RECUPERACAO!")