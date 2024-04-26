# Uma Variação do Método Noves Fora

A Prova dos noves (também conhecida como noves fora) é um método para
verificar erros realizados em uma operação de soma (na verdade pode
ser usado também em outras operações aritméticas). Esse método
consiste em tirar os noves dos números de entrada e saída da operação
aritmética. Para ser usado na verificação de somas, esse método é aplicado ao
valor resultante da soma como também ao valor das parcelas da soma. Os dois
resultados devem ser iguais.

Tirar os noves é somar os algarismos do número, dois a dois, sempre
tirando os noves. Por exemplo, o método aplicado ao número
751934 é 2. Veja a explicação detalhada:

    7 + 5 = 12, tirando 9, fica 3
    3 + 1 = 4
    4 + 9 = 13, tirando 9, fica 4
    4 + 3 = 7
    7 + 4 = 11, tirando 9, fica 2

É possível inferir que a aplicação do método em dois números distintos

que possuem os mesmos algarismos resulta no mesmo valor. Uma possível
implementação desse método é ordenar de forma decrescente os algarismos
do número (usar uma
lista para manter os algarismos ordenados) e proceder
a soma dos dois primeiros algarismos que seriam retirados da lista
com os algarismos. O valor resultante do método
noves fora aplicado a esta soma seria inserido na lista, mantendo a
ordenação.

Escreva a função <code>noves_fora(lista)</code> que recebe uma
lista ordenada de forma decrescente com os algarismos de um número
e que determina o valor resultante do método noves fora. A função
além de retornar o valor resultante do método ainda retorna uma lista
com a evolução da lista quando da aplicação do método.

## Atenção

Não use as funções de ordenação disponíveis em Python. Não é
permitido também usar insert(). Adicionar elementos apenas com
append().


## Exemplos e Asserts

O número 751934 seria representado pela lista [9, 7, 5, 4, 3, 1] que
é formada pelos algarismos do número em ordem decrescente.

O valor resultante do método seria 2, como mostrado acima e o histórico
de evolução seria o seguinte:

    [9, 7, 5, 4, 3, 1]
    [7, 5, 4, 3, 1] porque 9 + 7 é 16, noves fora 7
    [4, 3, 3, 1] porque 7 + 5 é 12, noves fora 3
    [7, 3, 1] porque 4 + 3 é 7, noves fora 7
    [1, 1] porque 7 + 3 é 10, noves fora 1
    [2] porque 1 + 1 é 2, noves fora 2 que é o valor final

Observe que em cada etapa da evolução, a lista está ordenada.

Veja exemplos de asserts:

```python
assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1],
                                              [7, 5, 4, 3, 1],
                                              [4, 3, 3, 1],
                                              [7, 3, 1],
                                              [1, 1],
                                              [2]])
assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])
```