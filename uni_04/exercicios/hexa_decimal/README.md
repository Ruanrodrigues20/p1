# Hexadecimal para decimal

Escreva um programa que converta um numeral hexadcimal no seu
equivalente decimal. O programa deve mostrar o passo a passo da
conversão.

## Entrada

A entrada consiste em uma única linha, contendo o numeral
hexadecimal (por simplicidade, apenas digitos de `0` a `9` e as
letras de `a` a `f` minúsculas são usadas para representar os
numerais em hexadecimal). Um exemplo de entrada é dado abaixo.

```
3f0a
```


## Saída

A saída consiste numa listagem com a decomposição digito a digito
do numeral lido da entrada, a correspondente conversão para
decimal de cada digito hexadecimal e, na última linha, o número
escrito nas duas bases: hexadecimal e o correspondente decimal.
Abaixo a saída correspondente à entrada acima.

```
3 * 16^3 = 12288
15 * 16^2 = 3840
0 * 16^1 = 0
10 * 16^0 = 10
---
3f0a(16) = 16138(10)
```

## Importante

Obviamente, nenhuma facilidade de python para conversão
de bases pode ser usada.

**Dica**: você pode usar o método `isdigit()` que diz se um
caractere (ou _string_) é ou não um digito decimal; e a função
`ord()` que retorna o código ASCII de um caractere qualquer.