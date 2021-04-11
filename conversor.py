from automato_finito_deterministico import AutomatoFinitoDeterministico
from automato_finito_nao_deterministico import AutomatoFinitoNaoDeterministico

class Conversor:

    def __init__(self):
        self.afd = AutomatoFinitoDeterministico()

    def conversao(self, afnd):
        mapeamento_subconjuntos = []
        indice_estado = 0
        controle = False

        self.afnd = afnd
        self.afd.alfabeto = self.afnd.alfabeto

        if self.afnd.estado_inicial == None:
            return print("Não é possível realizar a conversão!")

        self.afd.estados.append([self.afnd.estado_inicial])
        self.afd.estado_inicial = [self.afnd.estado_inicial]

        while controle == False:
            novos_estados_map_temp = []
            for simbolo in self.afnd.alfabeto:
                subconjunto = []
                if indice_estado > (len(self.afd.estados) - 1) :
                    controle = True
                    continue
                for estado_origem in self.afd.estados[indice_estado]:
                    for estado_destino in self.afnd.transicoes[estado_origem][simbolo]:
                        if estado_destino not in subconjunto:
                            subconjunto.append(estado_destino)

                for estado_destino in subconjunto:
                    if estado_destino in self.afnd.estados_finais:
                        if subconjunto not in self.afd.estados_finais:
                            self.afd.estados_finais.append(subconjunto)

                mapeamento_subconjuntos.append(subconjunto)
                novos_estados_map_temp.append(subconjunto)

            if indice_estado >= 0:
                for novo_estado in novos_estados_map_temp:
                    if novo_estado not in self.afd.estados:
                        self.afd.estados.append(novo_estado)

            if controle == False:
                indice_estado += 1

        self.afd.estado_inicial = '0'

        for novo_estado in range(len(self.afd.estados)):
            for subconjunto in range(len(mapeamento_subconjuntos)):
               if mapeamento_subconjuntos[subconjunto] == self.afd.estados[novo_estado]:
                    mapeamento_subconjuntos[subconjunto] = str(novo_estado)
            for estado_final in range(len(self.afd.estados_finais)):
                if self.afd.estados_finais[estado_final] == self.afd.estados[novo_estado]:
                    self.afd.estados_finais[estado_final] = str(novo_estado)
            self.afd.estados[novo_estado] = str(novo_estado)

        transicoes_afd = {}
        indice_resultado_subconjunto = 0

        for novo_estado in self.afd.estados:
            transicoes_afd[novo_estado] = {}
            for simbolo in self.afd.alfabeto:
                transicoes_afd[novo_estado][simbolo] = mapeamento_subconjuntos[indice_resultado_subconjunto]
                indice_resultado_subconjunto += 1

        self.afd.definir_transicoes(transicoes_afd)
        print("\nEstas são as informações do seu AFND convertido para AFD: ")
        print("Alfabeto: ", self.afd.alfabeto)
        print("Estados: ", self.afd.estados)
        print("Estado inicial: ", self.afd.estado_inicial)
        print("Estados finais: ", self.afd.estados_finais)
        print("Transições segue o padrão : {estado : {simbolo : destino}, }")
        print(self.afd.transicoes)