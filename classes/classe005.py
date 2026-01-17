class game():
    especie = "humano"
    def __init__(self, personagem, poder, pontuacao):
        self.personagem = personagem
        self.poder = poder
        self.pontuacao = pontuacao
    def apresentar(self):
        print(f"Personagem: {self.personagem} \nPoder: {self.poder} \nPontuacao: {self.pontuacao} \nEspecie: {game.especie} \n")
    @classmethod
    def change_especie(cls, new_especie):
        cls.especie = new_especie

n1 = game("Ana", "fogo", 73)
n2 = game("Zoid", "voar", 69)
n3 = game("Mega", "forca", 86)

n1.apresentar()
n2.apresentar()
n3.apresentar()

print("Mudando a especie...\n")
game.change_especie("Alienigena")

n1.apresentar()
n2.apresentar()
n3.apresentar()
