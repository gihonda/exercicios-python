nome = str(input("Digite seu nome completo: "))
partes = nome.split()
print(f"Ola {nome}!\nSeu primeiro nome e {partes[0]}")
print(f"Seu ultimo nome e {partes[-1]}")