# Desvio Padrão

Desvio padrão é uma medida de dispersão estatítica. Dada uma
sequência numérica, o desvio padrão mostra quão dispersa é essa
sequência. Por exemplo, o desvio padrão da sequência

    [1, 1, 1, 1, 2, 1, 2, 2, 2]

é menor do que o desvio padrão da sequência

    [1, 364564, 23, 12523656, -4343]

pois a _variância_ entre os valores é menor.

Faça um programa que leia duas sequências e que imprima qual a
sequência com o maior desvio padrão. A fórmula para calcular o
desvio padrão é dada pela figura abaixo.

![desvio padrão](http://www.dsc.ufcg.edu.br/~dalton/dropbox/images/stdev.png)

O cálculo é feito da seguinte maneira:

- Calcula-se a média dos elementos da sequência.
- Para cada valor da sequência, calcula-se a diferença entre o
  valor e a média calculada no passo anterior. Eleva-se cada uma
  dessas diferenças ao quadrado e calcula-se a soma resultante.
  Isto é, a soma dos quadrados das diferenças.
- Divide-se o resultado anterior por N - 1, onde N é a quantidade
  de elementos na sequência.
- Calcula-se a raiz do valor calculado no passo anterior.

## Entrada

Seu programa deve ler duas linhas da entrada padrão. Cada linha
corresponde a uma sequência de pelo menos 2 números.

## Saída

Na saída, seu programa deve imprimir qual das duas sequências
possui a maior variação (sequência 1 ou sequência 2), isto é, o
maior desvio padrão, além de imprimir esse desvio formatado com 2
casas decimais.

Caso elas possuam o mesmo desvio, deve imprimir a mensagem: As
sequências possuem o mesmo desvio padrão.

## Exemplo de execução

```
$ python solution.py
1 1 1.2 1 1 1.1 2
2 3 4 5 6
A sequência 2 possui o maior desvio padrão (1.58).

$ python solution.py
1 1
1 1
As sequências possuem o mesmo desvio padrão (0.00).
```