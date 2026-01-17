class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False  #comeca desligado

    def ligar(self):
        self.ligado = True
        print("O carro esta ligado!")

    def desligar(self):
        self.desligado = False
        print("O carro esta desligado!")

    def status(self):
        if self.ligado:
            print(f"{self.marca} {self.modelo} {self.ano} esta LIGADO!")
        else:
            print(f"{self.marca} {self.modelo} {self.ano} esta DESLIGADO!")

c1 = Carro("Toyota", "Esquire", 2019)
c1.status()
c1.ligar()
c1.status()
c1.desligar()
