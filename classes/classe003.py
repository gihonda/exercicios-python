class animal():
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    def apresentar(self):
        print(f"Ola, meu nome e {self.nome}, sou um {self.especie} e tenho {self.idade} anos. ")

animal1 = animal("Rex", "cachorro", 5)
animal2 = animal("Married", "gato", 7)

animal1.apresentar()
animal2.apresentar()
