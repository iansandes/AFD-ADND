# Leitor de Autômatos
## Atividade Prática para a Disciplina de Linguagens Formais e Autômatos - UNIT

## Rodando a solução

- Clone o repositório
- Certifique-se que tenha o python instalado
- Na raiz do projeto rode o comando python main.py
 ```sh
python main.py
```

## Como utilizar

O projeto é todo interativo e basta apenas seguir os as instruções pedidas para a montagem e verificação do autômato finito.

- Menu Interativo
````sh
============= AFD E AFND ==============
Selecione qual autômato você deseja montar e rodar:
1 - Autômato Finito Determinístico
2 - Autômato Finito Não Determinístico (Sem transação vazia)

Digite: 1
````

- Automato Finito Determinístico

Exemplo de AFD: 

AFD sobre Σ = {a, b} que considere
L = { w | w possui uma quantidade de caracteres impares }
tal que = ({q0, q1,}, Σ, δf, q0, {q1}).

```sh
============ AUTOMATO FINITO DETERMINÍSTICO============

Passo 1 - DEFINA SEU ALFABETO
Insira um simbolo no alfabeto do seu automato: a

1 - Adicionar outro simbolo ao autômato?
2 - Continuar

Digite: 1
----------------------

Simbolos cadastrados:  ['a']
Insira um simbolo no alfabeto do seu automato: b

1 - Adicionar outro simbolo ao autômato?
2 - Continuar

Digite: 2
----------------------

Simbolos cadastrados:  ['a', 'b']

Passo 2 - DEFINA OS ESTADOS (qN)
Insira um estado ao automato: q0

1 - Adicionar outro estado ao autômato
2 - Continuar

Digite: 1
Insira um estado ao automato: q1

1 - Adicionar outro estado ao autômato
2 - Continuar

Digite: 2

Passo 3 - DEFINA QUAL DOS ESTADOS SERÁ O ESTADO INICIAL (qN):
Estados cadastrados:  ['q0', 'q1']

Digite: q0
----------------------

Passo 4 - DEFINA OS ESTADOS FINAIS (qN)
Estados cadastrados:  ['q0', 'q1']

Insira um estado final ao seu automato: q1

1 - Adicionar outro estado final ao autômato
2 - Continuar construção do autômato

Digite: 2
----------------------

DEFINA AS TRANSIÇÕES DOS SEUS ESTADOS:

ESTADO ATUAL:  q0
Alfabeto:  ['a', 'b']
Digite a entrada para o estado q0: a

Estados cadastrados:  ['q0', 'q1']

Digite o ESTADO DESTINO caso a entrada a seja feita: q1

1 - Adicionar outra entrada para o estado  q0
2 - Continuar construção do autômato
Digite: 1
----------------------
ESTADO ATUAL:  q0
Alfabeto:  ['a', 'b']
Digite a entrada para o estado q0: b

Estados cadastrados:  ['q0', 'q1']

Digite o ESTADO DESTINO caso a entrada b seja feita: q1

1 - Adicionar outra entrada para o estado  q0
2 - Continuar construção do autômato
Digite: 2
----------------------
ESTADO ATUAL:  q1
Alfabeto:  ['a', 'b']
Digite a entrada para o estado q1: a

Estados cadastrados:  ['q0', 'q1']

Digite o ESTADO DESTINO caso a entrada a seja feita: q0

1 - Adicionar outra entrada para o estado  q1
2 - Continuar construção do autômato
Digite: 1
----------------------
ESTADO ATUAL:  q1
Alfabeto:  ['a', 'b']
Digite a entrada para o estado q1: b

Estados cadastrados:  ['q0', 'q1']

Digite o ESTADO DESTINO caso a entrada b seja feita: q1

1 - Adicionar outra entrada para o estado  q1
2 - Continuar construção do autômato
Digite: 2
----------------------

==================================================
Estas são as informações cadastradas no autômato:
Alfabeto: ['a', 'b']
Estados: ['q0', 'q1']
Estado inicial: q0
Estados finais: ['q1']

Confirmar? [S/N]
s
Montando o seu autômato!
.
.
.
Autômato pronto!

DEFINA UMA STRING PARA FAZER A VERIFICAÇÃO
Insira uma string para passar pelo autômato: a
.
.
.
A entrada 'a' é aceita pelo autômato proposto!

1 - Realizar outra verificação
2 - Finalizar

Digite: 1

Insira uma string para passar pelo autômato: aa
.
.
.
A entrada 'aa' NÃO é aceita pelo autômato proposto!

1 - Realizar outra verificação
2 - Finalizar

Digite: 1

Insira uma string para passar pelo autômato: aaaaa
.
.
.
A entrada 'aaaaa' é aceita pelo autômato proposto!

1 - Realizar outra verificação
2 - Finalizar

Digite: 2
```
- Automato Finito Não Determinístico

Neste caso, será informado um automato finito não determinístico sem transição vazia, ele será convertido internamente para um automato finito deterministico, impresso na tela, e você poderá inserir as strings para a verificação.

Exemplo de AFND: 

AFND sobre Σ = {0, 1} que considere
L = { w | w termine com em '01' }
tal que = ({q0, q1, q2}, Σ, δf, q0, {q2}).


```sh
============ AUTOMATO FINITO NÃO DETERMINÍSTICO============
O autômato será cadastrado normalmente, porém ele será transformado para um AFD e será feita a verificação das strings cadastradas.

Passo 1 - DEFINA SEU ALFABETO
Insira um simbolo no alfabeto do seu automato: 0

1 - Adicionar outro simbolo ao autômato?
2 - Continuar

Digite: 1
----------------------

Simbolos cadastrados:  ['0']
Insira um simbolo no alfabeto do seu automato: 1

1 - Adicionar outro simbolo ao autômato?
2 - Continuar

Digite: 2
----------------------

Simbolos cadastrados:  ['0', '1']

Passo 2 - DEFINA OS ESTADOS (qN)
Insira um estado ao automato: q0

1 - Adicionar outro estado ao autômato
2 - Continuar

Digite: 1
Insira um estado ao automato: q1

1 - Adicionar outro estado ao autômato
2 - Continuar

Digite: 1
Insira um estado ao automato: q2

1 - Adicionar outro estado ao autômato
2 - Continuar

Digite: 2

Passo 3 - DEFINA QUAL DOS ESTADOS SERÁ O ESTADO INICIAL (qN):
Estados cadastrados:  ['q0', 'q1', 'q2']

Digite: q0
----------------------

Passo 4 - DEFINA OS ESTADOS FINAIS (qN)
Estados cadastrados:  ['q0', 'q1', 'q2']

Insira um estado final ao seu automato: q2

1 - Adicionar outro estado final ao autômato
2 - Continuar construção do autômato

Digite: 2
----------------------

Passo 5 - DEFINA AS TRANSIÇÕES DOS ESTADOS:

ESTADO ATUAL:  q0
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q0: 0

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 0 seja feita: q0

1 - Adicionar outro estado de destino para a entrada 0
2 - Continuar construção do autômato

Digite: 1
----------------------

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 0 seja feita: q1

1 - Adicionar outro estado de destino para a entrada 0
2 - Continuar construção do autômato

Digite: 2
----------------------

1 - Adicionar outra entrada para o estado q0
2 - Continuar
Digite: 1
----------------------
ESTADO ATUAL:  q0
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q0: 1

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 1 seja feita: q0

1 - Adicionar outro estado de destino para a entrada 1
2 - Continuar construção do autômato

Digite: 2
----------------------

1 - Adicionar outra entrada para o estado q0
2 - Continuar
Digite: 2
----------------------
ESTADO ATUAL:  q1
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q1: 0

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 0 seja feita: SD

1 - Adicionar outra entrada para o estado q1
2 - Continuar
Digite: 1
----------------------
ESTADO ATUAL:  q1
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q1: 1

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 1 seja feita: q2

1 - Adicionar outro estado de destino para a entrada 1
2 - Continuar construção do autômato

Digite: 2
----------------------

1 - Adicionar outra entrada para o estado q1
2 - Continuar
Digite: 2
----------------------
ESTADO ATUAL:  q2
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q2: 0

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 0 seja feita: SD

1 - Adicionar outra entrada para o estado q2
2 - Continuar
Digite: 1
----------------------
ESTADO ATUAL:  q2
OBS: Mesmo que o estado não tenha as entradas ['0', '1'], insira elas e ao definir o estado destino, digite 'SD'!
Digite a ENTRADA para o estado q2: 1

Estados cadastrados:  ['q0', 'q1', 'q2']

Digite o ESTADO DESTINO caso a entrada 1 seja feita: SD

1 - Adicionar outra entrada para o estado q2
2 - Continuar
Digite: 2
----------------------

==================================================
Estas são as informações cadastradas no autômato:
Alfabeto: ['0', '1']
Estados: ['q0', 'q1', 'q2']
Estado inicial: q0
Estados finais: ['q2']

Confirmar? [S/N]
s
Montando o seu autômato!
.
.
.
Autômato pronto!
Estas são as informações do seu AFND convertido para AFD:
Alfabeto:  ['0', '1']
Estados:  ['0', '1', '2']
Estado inicial:  0
Estados finais:  ['2']
Transições:
{'0': {'0': '1', '1': '0'}, '1': {'0': '1', '1': '2'}, '2': {'0': '1', '1': '0'}}

DEFINA UMA STRING PARA FAZER A VERIFICAÇÃO
Insira uma string para passar pelo autômato: 01
.
.
.
A entrada '01' é aceita pelo autômato proposto!

1 - Realizar outra verificação
2 - Finalizar

Digite: 1

Insira uma string para passar pelo autômato: 0000
.
.
.
A entrada '0000' NÃO é aceita pelo autômato proposto!

1 - Realizar outra verificação
2 - Finalizar

Digite: 2
````
```
