import random
class Jogador:
    def __init__(self,nome):
        self.nome = nome
        self.pontos = 0
    def adicionar_pontos(self, valor):
        self.pontos += valor
    def mostrar_pontos(self):
        print(f"{self.nome} tem {self.pontos} pontos.")
class Rodada:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto
    def verificar_palpite(self, palpite):
        if palpite == self.numero_secreto:
            print("Acertou!")
            return True
        else:
            print("Errou!")
            return False
class Jogo:
    def __init__(self,jogador):
        self.jogador = jogador
    def iniciar(self):
        numero_secreto = random.randint(1,10)
        rodada = Rodada(numero_secreto)

        palpite = int(input("Advinhe um numero de 1 a 10: "))
        if rodada.verificar_palpite(palpite):
            self.jogador.adicionar_pontos(10)
        self.jogador.mostrar_pontos()

nome = input("Digite o nome do jogador: ")
jogador = Jogador(nome)
jogo = Jogo(jogador)
jogo.iniciar()
