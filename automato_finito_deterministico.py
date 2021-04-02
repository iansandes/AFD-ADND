class AutomatoFinitoDeterministico:
    def __init__(self):
        self.alfabeto = []
        self.estados = []
        self.estado_inicial = None
        self.estados_finais = []
        self.transicoes = {}

    def definir_alfabeto(self, alfabeto):
        self.alfabeto = alfabeto

    def definir_estado_inicial(self, estado):
        if estado in self.estados:
            self.estado_inicial = estado
        else:
            print("Estado inicial invalido")

    def definir_estados(self, estados):
        self.estados = estados
        self.estados.sort()

    def definir_estados_finais(self, estados):
        for estado in estados:
                if estado not in self.estados_finais:
                    self.estados_finais.append(estado)

    def definir_transicoes(self, transicoes):
        self.transicoes = transicoes

    def verificar_entrada(self, entrada):
        for simbolo in list(entrada):
            if simbolo not in self.alfabeto:
                print("O símbolo {simbolo_atual} não faz parte do alfabeto!".format(simbolo_atual= simbolo))
                return False

        estado_atual = self.estado_inicial

        if estado_atual != None:
            for simbolo in entrada:
                estado_atual = self.transicoes[estado_atual][simbolo]

            if estado_atual in self.estados_finais:
                return print("A entrada '{entrada}' é aceita pelo autômato proposto!".format(entrada=entrada))
            else:
                return print("A entrada '{entrada}' NÃO é aceita pelo autômato proposto!".format(entrada=entrada))
        else:
            print("Autômato inválido!")
