# Pivot

O algoritmo de ordenação conhecido por Quicksort é baseado em um
algoritmo recursivo que a cada recursão ordena apenas
parcialmente o vetor. Essa etapa consiste em escolher um valor
_pivot_ e em ordenar parcialmente o vetor em torno desse valor.
Após executar esse passo, o vetor se encontrará com todos os
valores menores que o pivot à esquerda do pivot e todos os
maiores à direita (valores iguais ao pivot ficarão todos juntos,
naturalmente, já que se trata de ordenação). Esse processo é
feito em uma única passada pelo vetor, o que significa que seu
tempo é linear.

Pede-se que você escreva uma função que implemente uma versão
simplificada do algoritmo de ordenação parcial baseada em um
pivot, que atue sobre uma lista python. A função deve receber
uma lista de inteiros e modificá-la de forma que os elementos
sejam parcialmente ordenados em relação ao pivot, que deve
ser o primeiro elemento da lista, se existir. Ou seja, todos
os elementos menores que o pivot à sua esquerda e os maiores,
à direita. Os valores maiores e menores devem preservar sua
ordem relativa no vetor.  Considere, por exemplo, o seguinte
vetor.

      [6, 4, 8, 1, 7, 3]

O algoritmo deve considerar que o vetor é o primeiro valor:
6. A modificação do vetor deve fazer com que todos os valores
menores que 6 fiquem à esquerda e os maiores à direita, mas
mantendo suas posições relativas originais. Assim, o vetor
resultante deve ser:

      [4, 1, 3, 6, 8, 7]

## Exemplos de asserts

      numeros = [6, 4, 8, 1, 7, 3]
      pivot(numeros)
      assert numeros == [4, 1, 3, 6, 8, 7]