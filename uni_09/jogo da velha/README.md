# Jogo da Velha

O Jogo da Velha é um tradicional jogo de tabuleiro que é jogado
por dois jogadores. O primeiro é representado por um círculo `O`
e a segunda representada por um xis `X`. O tabuleiro é sempre uma
matriz 3x3. As regras são bem simples: alternadamente, os
jogadores escolhem e marcam posições do tabuleiro.  Ganha aquele
que primeiro conquistar uma linha inteira, uma coluna inteira ou,
ainda, uma das diagonais.

Escreva a função `jogo_da_velha(tabuleiro)` que deve verificar se
houve vencedor de um jogo da velha e quem foi o vencedor. A
função recebe uma matriz 3x3 que representa um tabuleiro e uma
distribuição válida do jogo jogado pelos jogadores. Os jogadores
utilizam os símbolos `X` e `O`. Quando há um espaço vazio no
tabuleiro ele é representado pelo caractere `-`. O retorno da
função deve ser uma string: `X ganhou`, se houver uma sequencia
de 3 `X`s em alguma linha, coluna ou diagonal. De forma análoga,
deve ser `O ganhou`, se houver uma sequencia de 3 `O`s. E, por
fim, o retorno da função deve ser `Ninguem ganhou`, se não houver
vencedor.


## Exemplo e Asserts

```
jogo1 = [['O', 'O', 'X'],
         ['X', 'O', 'O'],
         ['O', 'O', 'X']]
assert jogo_da_velha(jogo1) == 'O ganhou'

jogo2 = [['O', 'X', 'X'],
         ['X', 'X', 'O'],
         ['O', 'O', 'X']]
assert jogo_da_velha(jogo2) == 'Ninguem ganhou'
```