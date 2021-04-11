class AutomatoFinitoNaoDeterministico:
    def __init__(self):
        self.alfabeto = []
        self.transicoes = {}
        self.estados = []
        self.estado_inicial = None
        self.estados_finais = []

    def definir_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def definir_estados(self, estados):
        self.estados = estados
        self.estados.sort()

    def definir_estado_inicial(self, estado):
        if estado in self.estados:
            self.estado_inicial = estado
        else:
            print("Estado inicial invalido")

    def definir_estados_finais(self, estados):
        for estado in estados:
                if estado not in self.estados_finais:
                    self.estados_finais.append(estado)

    def definir_transicoes(self, transicoes):
        self.transicoes = transicoes



