# Caixa Preta Descartando Leituras

Na análise dos dados de uma caixa preta é muito importante detectar
o momento em que houve falha na coleta de dados do peso, combustível
e altitude. Se qualquer um desses elementos for negativo, considera-se

que a partir daquele momento (incluindo o dado negativo)
as medições não são confiáveis e a leitura deve ser interrompida,
considerando apenas os valores válidos para análise.

Faça um programa que leia várias medições de peso, combustível e altitude
e determine o momento em que os dados passaram a ser considerados inválidos,
além de determinar quantos dados válidos
foram lidos de cada categoria (peso, combustível e altitude)

## Entrada

Seu programa deverá ler as medições até que um dos valores lidos seja negativo.
Em cada linha, são lidos peso, combustível e altitude (separados por espaço).

## Saída

Na saída, seu programa deve imprimir uma mesagem detalhando qual dado
foi considerado inválido, e a quantidade de dados válidos lidos para
cada categoria.

Dependendo do dado inválido, a mensagem pode variar. Veja
as três mensagens possíveis abaixo:

```
    - dado inconsistente. peso negativo.
    - dado inconsistente. combustível negativo.
    - dado inconsistente. altitude negativa.
```

## Restrições e Recursos permitidos

É permitido utilizar a função split.
Não é permitido utilizar a função map.

## Exemplo de execução

```
$ python solution.py
10 2 3
3 1 -1
dado inconsistente. altitude negativa.
peso: 2
combustível: 2
altitude: 1
```
```
$ python solution.py
1 2 4
-1 2 3
dado inconsistente. peso negativo.
peso: 1
combustível: 1
altitude: 1
```ca