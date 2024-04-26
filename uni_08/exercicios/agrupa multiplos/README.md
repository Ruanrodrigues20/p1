# Agrupa Múltiplos

Pede-se que você escreva a função `agrupa_multiplos(seq, k)`
que altera uma dada sequência `seq` de números inteiros, de
forma que todos os valores divisíveis por `k` sejam relocados
para o início da lista (assuma que `k > 0`). Por exemplo, ao
invocar a função para a sequência

```
6 15 12 6 8 3 25 14 1 10 7
```

e para o valor `k` igual a 5, a sequência será alterada para

```
15 25 10 6 12 6 8 3 14 1 7
```

Observe que a ordem dos múltiplos, bem como a dos não
múltiplos dentro de cada categoria é preservada. Observe nos
asserts abaixo que se espera que a função tenha efeito
colateral.

## Exemplos de asserts

```
seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]
agrupa_multiplos(seq, 5)
assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]
agrupa_multiplos(seq, 2)
assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]
```