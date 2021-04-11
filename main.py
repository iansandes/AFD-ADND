from collections import defaultdict
from time import sleep


from automato_finito_deterministico import AutomatoFinitoDeterministico
from automato_finito_nao_deterministico import AutomatoFinitoNaoDeterministico
from conversor import Conversor

def menu_inicial():
    print("============= AFD E AFND ==============")
    print("Selecione qual autômato você deseja montar e rodar: ")
    print("1 - Autômato Finito Determinístico")
    print("2 - Autômato Finito Não Determinístico (Sem transação vazia)")
    resultado = input("\nDigite: ")
    if int(resultado) != 1 and int(resultado) != 2:
        print("\nOpção Inválida!")
        return None

    return int(resultado)

def sleep_loading():
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)

def main():
    opcao = menu_inicial()

    if opcao == None:
        return opcao

    if opcao == 1:
        print("\n============ AUTOMATO FINITO DETERMINÍSTICO============")
        afd = AutomatoFinitoDeterministico()

        opcao_alfabeto = 1
        alfabeto = []
        print("\nPasso 1 - DEFINA SEU ALFABETO")
        while opcao_alfabeto == 1:
            caractere = input("Insira um simbolo no alfabeto do seu automato: ")
            alfabeto.append(caractere)
            print("\n1 - Adicionar outro simbolo ao autômato?")
            print("2 - Continuar")
            opcao_alfabeto = int(input("\nDigite: "))
            print("----------------------")
            print()
            print("Simbolos cadastrados: ", alfabeto)

        afd.definir_alfabeto(alfabeto)

        opcao_estados = 1
        estados = []
        print("\nPasso 2 - DEFINA OS ESTADOS (qN)")
        while opcao_estados == 1:
            caractere = input("Insira um estado ao automato: ")
            estados.append(caractere)
            print("\n1 - Adicionar outro estado ao autômato")
            print("2 - Continuar")
            opcao_estados = int(input("\nDigite: "))

        afd.definir_estados(estados)

        print("\nPasso 3 - DEFINA QUAL DOS ESTADOS SERÁ O ESTADO INICIAL (qN): ")
        print("Estados cadastrados: ", estados)
        estado_inicial = str(input("\nDigite: "))
        afd.definir_estado_inicial(estado_inicial)
        print("----------------------")


        opcao_estados_finais = 1
        estados_finais = []
        print("\nPasso 4 - DEFINA OS ESTADOS FINAIS (qN)")
        print("Estados cadastrados: ", estados)
        while opcao_estados_finais == 1:
            caractere = input("\nInsira um estado final ao seu automato: ")
            estados_finais.append(caractere)
            print("\n1 - Adicionar outro estado final ao autômato")
            print("2 - Continuar construção do autômato")
            opcao_estados_finais = int(input("\nDigite: "))
            print("----------------------")

        afd.definir_estados_finais(estados_finais)

        transicoes = defaultdict(dict)
        print("\nDEFINA AS TRANSIÇÕES DOS SEUS ESTADOS: \n")
        for estado in estados:
            opcao_transicoes = 1
            while opcao_transicoes == 1:
                print("ESTADO ATUAL: ", estado)
                print("Alfabeto: ", alfabeto)
                entrada = input("Digite a entrada para o estado {estado_atual}: ".format(estado_atual = estado))
                print("\nEstados cadastrados: ", estados)
                proximo_estado = input("\nDigite o ESTADO DESTINO caso a entrada {entrada} seja feita: ".format(entrada = entrada))
                transicoes[estado][entrada] = proximo_estado
                print("\n1 - Adicionar outra entrada para o estado ", estado)
                print("2 - Continuar construção do autômato")
                opcao_transicoes = int(input("Digite: "))
                print("----------------------")

        afd.definir_transicoes(transicoes)

        print("\n==================================================")
        print("Estas são as informações cadastradas no autômato: ")
        print("Alfabeto:", afd.alfabeto)
        print("Estados:", afd.estados)
        print("Estado inicial:", afd.estado_inicial)
        print("Estados finais:", afd.estados_finais)

        confirmacao = 1
        while confirmacao == 1:
            print("\nConfirmar? [S/N]")
            confirmacao = input()
            if confirmacao.upper() != 'N' and confirmacao.upper() != 'S':
                print("Opção inválida!")
                confirmacao == 1
                continue
            if confirmacao.upper() == 'N':
                main()

        print("Montando o seu autômato!")
        sleep_loading()
        print("Autômato pronto!")
        sleep(1)

        opcao_verificar = 1
        print("\nDEFINA UMA STRING PARA FAZER A VERIFICAÇÃO")
        while opcao_verificar == 1:
            string_entrada = input("Insira uma string para passar pelo autômato: ")
            sleep_loading()
            afd.verificar_entrada(string_entrada)
            print("\n1 - Realizar outra verificação")
            print("2 - Finalizar")
            opcao_verificar = int(input("\nDigite: "))
            print()

    if opcao == 2:
        print("\n============ AUTOMATO FINITO NÃO DETERMINÍSTICO============")
        print("O autômato será cadastrado normalmente, porém ele será transformado para um AFD e será feita a verificação das strings cadastradas.")
        afnd = AutomatoFinitoNaoDeterministico()

        opcao_alfabeto = 1
        alfabeto = []
        print("\nPasso 1 - DEFINA SEU ALFABETO")
        while opcao_alfabeto == 1:
            caractere = input("Insira um simbolo no alfabeto do seu automato: ")
            alfabeto.append(caractere)
            print("\n1 - Adicionar outro simbolo ao autômato?")
            print("2 - Continuar")
            opcao_alfabeto = int(input("\nDigite: "))
            print("----------------------")
            print()
            print("Simbolos cadastrados: ", alfabeto)

        afnd.definir_alfabeto(alfabeto)

        opcao_estados = 1
        estados = []
        print("\nPasso 2 - DEFINA OS ESTADOS (qN)")
        while opcao_estados == 1:
            caractere = input("Insira um estado ao automato: ")
            estados.append(caractere)
            print("\n1 - Adicionar outro estado ao autômato")
            print("2 - Continuar")
            opcao_estados = int(input("\nDigite: "))


        afnd.definir_estados(estados)

        print("\nPasso 3 - DEFINA QUAL DOS ESTADOS SERÁ O ESTADO INICIAL (qN): ")
        print("Estados cadastrados: ", estados)
        estado_inicial = str(input("\nDigite: "))
        afnd.definir_estado_inicial(estado_inicial)
        print("----------------------")

        opcao_estados_finais = 1
        estados_finais = []
        print("\nPasso 4 - DEFINA OS ESTADOS FINAIS (qN)")
        print("Estados cadastrados: ", estados)
        while opcao_estados_finais == 1:
            caractere = input("\nInsira um estado final ao seu automato: ")
            estados_finais.append(caractere)
            print("\n1 - Adicionar outro estado final ao autômato")
            print("2 - Continuar construção do autômato")
            opcao_estados_finais = int(input("\nDigite: "))
            print("----------------------")

        afnd.definir_estados_finais(estados_finais)

        transicoes = defaultdict(dict)
        print("\nPasso 5 - DEFINA AS TRANSIÇÕES DOS ESTADOS: \n")
        for estado in estados:
            opcao_transicoes = 1
            opcao_entradas = 1
            while opcao_transicoes == 1:
                opcao_entradas = 1
                lista_destinos = []
                print("ESTADO ATUAL: ", estado)
                print("OBS: Mesmo que o estado não tenha as entradas {alfabeto}, insira elas e ao definir o estado destino, digite 'SD'!".format(alfabeto=alfabeto))
                entrada = input("Digite a ENTRADA para o estado {estado_atual}: ".format(estado_atual = estado))
                while opcao_entradas == 1:
                    print("\nEstados cadastrados: ", estados)
                    proximo_estado = input("\nDigite o ESTADO DESTINO caso a entrada {entrada} seja feita: ".format(entrada = entrada))
                    if proximo_estado.upper() == 'SD':
                        opcao_entradas = 2
                        continue
                    lista_destinos.append(proximo_estado)
                    print("\n1 - Adicionar outro estado de destino para a entrada", entrada)
                    print("2 - Continuar construção do autômato")
                    opcao_entradas = int(input("\nDigite: "))
                    print("----------------------")

                transicoes[estado][entrada] = lista_destinos
                print("\n1 - Adicionar outra entrada para o estado", estado)
                print("2 - Continuar")
                opcao_transicoes = int(input("Digite: "))
                print("----------------------")

        afnd.definir_transicoes(transicoes)
        print("\n==================================================")
        print("Estas são as informações cadastradas no autômato: ")
        print("Alfabeto:", afnd.alfabeto)
        print("Estados:", afnd.estados)
        print("Estado inicial:", afnd.estado_inicial)
        print("Estados finais:", afnd.estados_finais)

        confirmacao = 1
        while confirmacao == 1:
            print("\nConfirmar? [S/N]")
            confirmacao = input()
            if confirmacao.upper() != 'N' and confirmacao.upper() != 'S':
                print("Opção inválida!")
                confirmacao == 1
                continue
            if confirmacao.upper() == 'N':
                main()

        print("Montando o seu autômato!")
        sleep_loading()
        print("Autômato pronto!")
        sleep(1)
        conversor = Conversor()
        conversor.conversao(afnd)

        opcao_verificar = 1
        print("\nDEFINA UMA STRING PARA FAZER A VERIFICAÇÃO")
        while opcao_verificar == 1:
            string_entrada = input("Insira uma string para passar pelo autômato: ")
            sleep_loading()
            conversor.afd.verificar_entrada(string_entrada)
            print("\n1 - Realizar outra verificação")
            print("2 - Finalizar")
            opcao_verificar = int(input("\nDigite: "))
            print()


if __name__ == "__main__":
    main()