# Conversão de Número na Base 2 para a Base 10

Escreva um programa que converte um número binário em um
número decimal.

## Entrada

O programa deve ler da entrada um
único número binário.

## Saída

O programa deve imprimir na saída a
decomposição bit a bit do número, a correspondente
conversão para decimal de cada bit e, na última linha, o
número escrito na base binária e o correspondente na
base decimal.

## Exemplo de Execução

No exemplo abaixo, observe que o número lido da entrada
`10111` (que está em binário) é convertido passo a passo para
o valor decimal `23` correspondente. Em cada linha da saída
vemos a conversão de um dos bits, começando do mais
significativo (valor `16`) até o menos significativo (valor
`1`). E na última linha vemos as duas representações do número
em binário e em decimal. Observe que o valor decimal
resultante corresponde à soma dos valores de cada linha
anterior.

```
$ python base2_10.py
10111
1 * 16 = 16
0 * 8 = 0
1 * 4 = 4
1 * 2 = 2
1 * 1 = 1
10111(2) = 23(10)
```ca