# Duplicados

Escreva um programa que identifica se uma dada sequência de valores
inteiros está duplicada e imprime a lista *deduplicada*, ou seja, só com
os valores não duplicados. Uma lista é dita duplicada se os valores da
primeira metade forem exatamente iguais aos valores da segunda metade da
sequência em diante. Assim, por exemplo, é duplicada as sequência:

    6 9 3 8 6 9 3 8

Enquanto que estas não são:

    1 2 3 1 2 4
    1 2 3 2 1

## Entrada

A entrada consiste em uma única linha, contendo os valores da
sequência, separados por espaços.

## Saída

A saída consiste em uma linha contendo os valores únicos, caso a lista
seja, de fato, duplicada, ou todos os valores da lista, caso não haja
duplicação.

## Restrições

- você PODE usar <code>split()</code>
- você NÃO pode usar <code>map()</code>
- você não pode usar *list comprehensions*

## Exemplo de execução

    $ python deduplica.py
    6 9 3 8 6 9 3 8
    6 9 3 8
    $

    $ python deduplica.py
    1 2 3 2 1
    1 2 3 2 1
    $