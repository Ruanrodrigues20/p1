# Acima da média (Criminalidade)

Um delegado precisa fazer um relatório anual das ocorrências
registradas em sua delegacia. Para facilitar a escrita do relatório,
ele deseja selecionar os meses em que a média de ocorrências por dia
for maior que a média estabelecida pela secretaria de segurança pública (ssp).

Pede-se que você escreva um programa que leia a média mensal estabelecida pela secretaria
de segurança pública e várias sequencias de valores
que representam a quantidade de ocorrências registradas por dia na delegacia.
Seu programa deve imprimir na saída apenas as sequências cuja média mensal é maior
que o estabelecido.

Você não deve assumir que serão lidos 30 ou 31 registros por linha. Tipicamente,
os delegados esquecem de registrar ou dados são perdidos.

## Entrada de dados

A entrada consiste em um texto contendo: 1) na primeira linha
o valor da média mensal estabelecida pela ssp; 2) nas linhas
seguintes, as sequências de valores a serem processados; 3)
uma linha contendo a palavra 'fim', indicando o fim
da entrada.

Importante: o programa também deve parar de ler a
entrada quando receber uma sequência de valores cuja média
seja 2 vezes menor que o valor limite indicado na primeira
linha da entrada. Todos os valores são expressos em
número de ocorrências, como inteiros. No entanto, a média é expressa
como float.

## Saída de dados

A saída consiste em uma linha para cada sequência cuja média seja
maior que o valor limite. Cada uma das linhas contém os
mesmos valores lidos da entrada.

## Exemplos de execução

    $ python joao.py
    100.0
    77 72 65
    101 110
    fim
    101 110

    $ python joao.py
    20.0
    120 110 12
    9 8
    120 110 12ca