class people():
    especie = "Humano"  #atributo de CLASSE (compartilhado por todos)
    def __init__(self, name, age):
        self.name = name  #atributo de INSTANCIA(cada objeto tem o seu)
        self.age = age
    def apresentar(self):
        print(f"Hello, my name is {self.name}, i'm {self.age} years old and i'm {people.especie}! ")
    @classmethod
    def change_class_especie(cls, new_especie):
        cls.especie = new_especie

p1 = people("Giovanna", 29)
p2 = people("Matheus", 32)
p1.apresentar()
p2.apresentar()

print("\nChanging the especie...\n")
people.change_class_especie("Ciborgue")

p1.apresentar()
p2.apresentar()
