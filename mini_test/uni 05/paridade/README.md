# Paridade

Paridade refere-se ao número de bits '1' de um determinado número binário.
Na paridade par, quando o número de bits de valor '1' for ímpar, é adicionado
um bit de valor '1' ao final da sequência, tornando o número de bits '1' par.
Quando o número de bits de valor '1' é par, é adicionado um bit de valor '0' ao
final da sequência. Este bit adicional chama-se de bit de paridade.

Exemplos: Considere as sequências: 10, 1101, 11101, 0 e 1. Após o cálculo de
paridade, teremos: 10(1), 1101(1), 11101(0), 0(0) e 1(1). O bit menos significativo (LSB)
representado nos exemplos entre parenteses é o bit de paridade acrescentado à
sequencia de bits original.

A paridade é utilizada para detectar erros nas transmissões, já que o seu cálculo
é extremamente simples. Nos exemplos anteriores, seriam considerados erros de paridade
se, para as sequências apresentadas, tivéssemos obtido os valores: 10(0), 1101(0),
11101(1), 0(1) e 1(0).

Escreva um programa que receba uma sequência de valores binários com tamanho maior ou
igual a **2**. Considerando que o último bit é o bit de paridade (já incluso na sequencia
de bits), seu programa deve parar quando receber uma sequência com erro na paridade.

## Entrada

Cada linha representa uma sequência binária. O LSB (bit menos significativo) representa
o bit de paridade.

## Saída

O programa deve parar quando for detectado erro na paridade, ou seja, o  bit de paridade
adicionado está errado. O programa deve informar a mensagem "ERRO" seguido da seequencia
de bits errada. Veja exemplo abaixo para entender a formatação de saída.

## Exemplo
```
python paridade.py
101
100
ERRO: 100
```

```
python paridade.py
11011
111010
00
11
10
ERRO: 10
```
