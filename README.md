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

Exemplo de AFD: 

AFN sobre Σ = {a, b} que considere
L = { w | w possui uma quantidade de caracteres impares }
tal que = ({q0, q1,}, Σ, δf, q0, {q1}).

```sh
DEFINA SEU ALFABETO
Insira um caractere no alfabeto do seu automato: a
Digite '1' para adicionar outro caractere em seu alfabeto, ou digite '2' para prosseguir com a construção do seu autômato: 1

Insira um caractere no alfabeto do seu automato: b
Digite '1' para adicionar outro caractere em seu alfabeto, ou digite '2' para prosseguir com a construção do seu autômato: 2

DEFINA SEUS ESTADOS SEGUINDO O EXEMPLO AO LADO -----> qN
Insira um estado ao seu automato: q0
Digite '1' para adicionar outro estado em seu autômato, ou digite '2' para prosseguir com a construção do seu autômato: 1

Insira um estado ao seu automato: q1
Digite '1' para adicionar outro estado em seu autômato, ou digite '2' para prosseguir com a construção do seu autômato: 2

DEFINA QUAL DOS SEUS ESTADOS SERÁ O ESTADO INICIAL SEGUINDO O EXEMPLO AO LADO -----> qN:
['q0', 'q1']
q0
DEFINA SEUS ESTADOS FINAIS SEGUINDO O EXEMPLO AO LADO -----> qN
['q0', 'q1']
Insira um estado final ao seu automato: q1
Digite '1' para adicionar outro estado final em seu autômato, ou digite '2' para prosseguir com a construção do seu autômato: 2

DEFINA AS TRANSIÇÕES DOS SEUS ESTADOS:

ESTADO ATUAL:  q0
Digite a entrada para o estado q0: a
Digite para qual estado irá caso essa entrada seja feita, seguindo o exemplo ao lado -----> qN: q1
Digite '1' para adicionar outra entrada para esse estado, ou digite '2' para prosseguir com a construção do seu autômato: 1

Digite a entrada para o estado q0: b
Digite para qual estado irá caso essa entrada seja feita, seguindo o exemplo ao lado -----> qN: q1
Digite '1' para adicionar outra entrada para esse estado, ou digite '2' para prosseguir com a construção do seu autômato: 2

ESTADO ATUAL:  q1
Digite a entrada para o estado q1: a
Digite para qual estado irá caso essa entrada seja feita, seguindo o exemplo ao lado -----> qN: q0
Digite '1' para adicionar outra entrada para esse estado, ou digite '2' para prosseguir com a construção do seu autômato: 1

Digite a entrada para o estado q1: b
Digite para qual estado irá caso essa entrada seja feita, seguindo o exemplo ao lado -----> qN: q0
Digite '1' para adicionar outra entrada para esse estado, ou digite '2' para prosseguir com a construção do seu autômato: 2

DEFINA UMA STRING PARA FAZER A VERIFICAÇÃO
Insira uma string para passar pelo autômato: a
A entrada 'a' é aceita pelo autômato proposto!
Digite '1' para verificar outra string em seu autômato, ou digite '2' para finalizar: 1

Insira uma string para passar pelo autômato: ab
A entrada 'ab' NÃO é aceita pelo autômato proposto!
Digite '1' para verificar outra string em seu autômato, ou digite '2' para finalizar: 1

Insira uma string para passar pelo autômato: aab
A entrada 'aab' é aceita pelo autômato proposto!
Digite '1' para verificar outra string em seu autômato, ou digite '2' para finalizar: 1

Insira uma string para passar pelo autômato: abab
A entrada 'abab' NÃO é aceita pelo autômato proposto!
Digite '1' para verificar outra string em seu autômato, ou digite '2' para finalizar: 2
```
