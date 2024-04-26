# Expressão de Soma

Escreva um programa que a partir de dois números inteiros
não-negativos `a` e `b` calcula o valor da soma `a + b + ab +
ba + bbb`, onde `xy` denota a concatenação dos dígitos dos
números `x` e `y`. Por exemplo, se `a` for 1 e `b` for 5, a
expressão da soma será 1 + 5 + 15 + 51 + 555 e o valor
calculado será 627. Os números `a` e `b` podem ter mais de um
digito. Por exemplo, `a` pode ser 2 e `b` pode ser `15`. Neste
caso, a expressão seria 2 + 15 + 215 + 152 + 151515, com valor
resultante 151899.

## Entrada

A entrada do programa consiste em duas linhas, contendo
exatamente os valores inteiros `a` e `b`, um em cada linha.

## Saída

A saída do programa deve imprimir apenas valor inteiro resultante da soma `a + b + ab + ba + bbb`.

## Exemplo de Entrada e Saída

```
$ python solution.py
1
5
627
```

```
$ python solution.py
2
15
151899
```