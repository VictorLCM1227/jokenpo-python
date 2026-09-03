# jogador

class Jogador:

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.partidas = 0
        self.taxa_de_vitorias = 0.0

    def registrar_resultado(self, resultado):

        self.partidas += 1

        if resultado == 'vitoria':
            self.vitorias += 1

        elif resultado == 'derrota':
            self.derrotas += 1

        elif resultado == 'empate':
            self.empates += 1

        self.calcular_taxa()

    def calcular_taxa(self):

        if self.partidas > 0:
            self.taxa_de_vitorias = (
                self.vitorias / self.partidas
            ) * 100

        else:
            self.taxa_de_vitorias = 0.0