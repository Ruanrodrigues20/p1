2# MinMax Sort = Selection Sort Duplicado

MinMax Sort é um algoritmo de ordenação baseado em comparação,
considerado uma variação do Selection Sort.
O MinMax Sort difere do Selection Sort pelo fato de selecionar
dois elementos em cada iteração. Inicialmente,
a partir do primeiro elemento, o menor elemento da lista é selecionado
e trocado com o elemento da primeira posição. Para completar a iteração,
o maior elemento é selecionado e trocado com o elemento da última posição.
Na iteração seguinte, as duas seleções são repetidas considerando os
elementos que estão entre a segunda e penúltima posições da lista, uma vez
que o primeiro e o último já estão em suas posições finais depois da iteração
anterior. O processo é repetido até que não seja mais necessário selecionar mais
elementos.

Perceba que em cada iteração dois elementos são ajustados para a sua posição
final na lista ordenada (um no início e outro no fim). No Selection Sort, apenas
um elemento é ajustado em cada iteração. Logo, o número de iterações no MinMax Sort
é menor.

Escreva a função `minmax_sort(lista)` que recebe uma
lista de inteiros e que ordena essa lista de inteiros. Essa função
retorna uma lista de listas que contem o status da lista após
cada passagem bidirecional.

Considere que a lista a ser ordenada tem pelo menos dois elementos.

## Ilustração do MinMax Sort

Considere que a lista recebida seja `[7, 4, 8, 1, 2, 3]`.

Na primeira iteração, o menor valor é `1` que é trocado com o valor `7` que está na
primeira posição. Em seguida, o maior valor `8` é trocado com o valor `3` que está
na última posição. Assim, ao final da primeira iteração a lista recebida tem a
seguinte configuração: `[1, 4, 3, 7, 2, 8]`.

A segunda iteração escolhe o menor e maior valores entre a segunda e penúltima posições
e efetua as respectivas trocas. Ao final da segunda iteração, a lista tem a seguinte
configuração: `[1, 2, 3, 4, 7, 8]`.

Na terceira e última iteração, o processo é repetido e a lista final tem a seguinte
configuração: `[1, 2, 3, 4, 7, 8]`.

## Atenção

Não use as funções de ordenação disponíveis em Python. Ordenar
in place apenas usando troca de elementos, ou seja, não use lista auxiliar,
não acrescente nem remova elementos da lista original. Não é permitido usar
as funções min() e max() de Python.


## Exemplos e Asserts

```
assert minmax_sort([7, 4, 8, 1, 2, 3]) == [[1, 4, 3, 7, 2, 8],
        [1, 2, 3, 4, 7, 8],
        [1, 2, 3, 4, 7, 8]]
```