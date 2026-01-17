from datetime import date
today = date.today().year
maior = 0
menor = 0
for pessoa in range(1,7):
    ano = int(input(f"Em que ano a {pessoa} nasceu? "))
    idade = today - ano
    if idade > 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade.")
print(f"E tambem tivemos {menor} pessoas menores de idade.")