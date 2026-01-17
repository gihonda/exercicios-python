class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola! Meu nome e {self.nome} e tenho {self.idade} anos. ")

p1 = Pessoa("Giovanna", 29)
p2 = Pessoa("Matheus", 32)

p1.apresentar()
p2.apresentar()