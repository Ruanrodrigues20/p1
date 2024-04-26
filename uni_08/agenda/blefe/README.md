# Blefe

Blefar significa enganar, fingir ou fazer alguém acreditar em
mentiras.  Escreva a função `blefe(array)` que recebe um array
de números inteiros e que altera os valores de alguns de seus
elementos fazendo com que o array fique em ordem decrescente.

A ideia a ser utilizada na implementação de `blefe` é reduzir os
valores que interfiram na ordem, forçando-os a manterem a ordem.
Assim, se um elemento não é menor que o anterior, ele deve ser
substituído por valor igual ao anterior, garantindo a ordem. O
processo deve ser repetido até o final do array.

Por exemplo, se o array inicial é formado pelos valores 9 4 5 3
1, o terceiro elemento do array será alterado para 4, de forma
que o array passe a ser 9 4 4 3 1 e tenha ordem decrescente.
Perceba que a lógica pode provocar uma propagação do efeito. Por
exemplo, após a aplicação do algoritmo, o array 15 9 4 5 2 1 3 4
deve ser alterado para 15 9 4 4 2 1 1 1.

## Semântica da função

A função opera sobre um array e tem efeito colateral. Além disso,
a função retorna um array da mesma dimensão que o array inicial,
contendo as diferenças entre os elementos originais e os novos.
Para melhor entendimento, veja os asserts no arquivo de testes
fornecido.

## Atenção

Esta operação **não deve** usar qualquer forma de ordenação. Nem
as facilidades de python, nem implementações pessoais de
algoritmos de ordenação (bubblesort, insertion-sort, etc).
