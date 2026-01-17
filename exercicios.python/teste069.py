tot18 = toth = totm = 0
while True:
    print("-" * 40)
    print("CADASTRE UMA PESSOA".center(40))
    print("-" * 40)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Sexo [F/M]: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F":
        if idade < 18:
            totm += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Ao todo tivemos {tot18} pessoas maiores de idade.")
print(f"Ao todo temos {toth} homens cadastrado.")
print(f"Temos {totm} mulheres com menos de 18 anos.")
print("Fim do programa!")
