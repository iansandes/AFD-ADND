from collections import defaultdict


from automato_finito_deterministico import AutomatoFinitoDeterministico

def main():
    afd = AutomatoFinitoDeterministico()

    opcao_alfabeto = 1
    alfabeto = []
    print("DEFINA SEU ALFABETO")
    while opcao_alfabeto == 1:
        caractere = input("Insira um caractere no alfabeto do seu automato: ")
        alfabeto.append(caractere)
        opcao_alfabeto = int(input("Digite '1' para adicionar outro caractere em seu alfabeto, ou digite '2' para prosseguir com a construção do seu autômato: "))
        print()

    afd.definir_alfabeto(alfabeto)


    opcao_estados = 1
    estados = []
    print("DEFINA SEUS ESTADOS SEGUINDO O EXEMPLO AO LADO -----> qN")
    while opcao_estados == 1:
        caractere = input("Insira um estado ao seu automato: ")
        estados.append(caractere)
        opcao_estados = int(input("Digite '1' para adicionar outro estado em seu autômato, ou digite '2' para prosseguir com a construção do seu autômato: "))
        print()

    afd.definir_estados(estados)

    print("DEFINA QUAL DOS SEUS ESTADOS SERÁ O ESTADO INICIAL SEGUINDO O EXEMPLO AO LADO -----> qN: ")
    print(estados)
    estado_inicial = str(input())
    afd.definir_estado_inicial(estado_inicial)


    opcao_estados_finais = 1
    estados_finais = []
    print("DEFINA SEUS ESTADOS FINAIS SEGUINDO O EXEMPLO AO LADO -----> qN")
    print(estados)
    while opcao_estados_finais == 1:
        caractere = input("Insira um estado final ao seu automato: ")
        estados_finais.append(caractere)
        opcao_estados_finais = int(input("Digite '1' para adicionar outro estado final em seu autômato, ou digite '2' para prosseguir com a construção do seu autômato: "))
        print()

    afd.definir_estados_finais(estados_finais)

    transicoes = defaultdict(dict)
    print("DEFINA AS TRANSIÇÕES DOS SEUS ESTADOS: \n")
    for estado in estados:
        opcao_transicoes = 1
        print("ESTADO ATUAL: ", estado)
        while opcao_transicoes == 1:
            entrada = input("Digite a entrada para o estado {estado_atual}: ".format(estado_atual = estado))
            proximo_estado = input("Digite para qual estado irá caso essa entrada seja feita, seguindo o exemplo ao lado -----> qN: ")
            transicoes[estado][entrada] = proximo_estado
            opcao_transicoes = int(input("Digite '1' para adicionar outra entrada para esse estado, ou digite '2' para prosseguir com a construção do seu autômato: "))
            print()

    afd.definir_transicoes(transicoes)


    opcao_verificar = 1
    print("DEFINA UMA STRING PARA FAZER A VERIFICAÇÃO")
    while opcao_verificar == 1:
        string_entrada = input("Insira uma string para passar pelo autômato: ")
        afd.verificar_entrada(string_entrada)
        opcao_verificar = int(input("Digite '1' para verificar outra string em seu autômato, ou digite '2' para finalizar: "))
        print()



if __name__ == "__main__":
    main()