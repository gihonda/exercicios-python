sexo = str(input("Informe o seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in "FM":
    sexo = str(input("Dados invalidos. Por favor, informe o seu sexo: ")).strip().upper()[0]
print(f"Sexo {sexo} cadastrado com sucesso!")
