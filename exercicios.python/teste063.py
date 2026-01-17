print(">"*40)
print("Sequenciade Fibonacci".center(40))
print(">"*40)
n = int(input("Quantos termos vc que mostrar? "))
primeirotermo = 0
segundotermo = 1
print("~"*40)
print(f"{primeirotermo} -> {segundotermo}", end="")
cont = 3
while cont <= n:
    terceirotermo = primeirotermo + segundotermo
    print(f" -> {terceirotermo}", end="")
    primeirotermo = segundotermo
    segundotermo = terceirotermo
    cont += 1
print(" -> FIM")
print("~"*40)