media = 0
maisvelho = 0
nomemaisv = ""
mulher = 0
for pess in range(1,5):
    print(f" {pess} PESSOA ".center(20,"="))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()
    media += idade
    if sexo == "F":
        if idade < 20:
            mulher += 1
    if sexo == "M":
        if pess == 1:
            maisvelho = idade
            nomemaisv = nome
        else:
            if idade > maisvelho:
                 maisvelho = idade
                 nomemaisv = nome
print(f"A media de idade do grupo e de {media / 4} anos")
print(f"O homem mais velho tem {maisvelho} anos e se chama {nomemaisv}")
print(f"Ao todo sao {mulher} mulheres menores de 20 anos.")