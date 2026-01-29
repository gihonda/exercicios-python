alunos = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    cont = str(input("Quer continuar? [S/N] ")).strip().upper()
    if cont in "N":
        break
print("-=" * 30)
print(f"{"No.":<4}{"Nome":<10}{"Media":>8}")
print("-" * 26)
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")
print("-" * 26)
while True:
    opc = int(input("Mostrar notas de qual aluno? (999 para interromper): "))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(alunos) - 1:
        print(f"Notas de {alunos[opc][0]} sao {alunos[opc][1]}")
        print("-" * 26)
print(">>> VOLTE SEMPRE <<<")
