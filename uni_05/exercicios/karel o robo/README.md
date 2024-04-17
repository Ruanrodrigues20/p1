# Karel, o Robô

No jogo, "Karel, o robô", a principal ação é conduzir um pequeno
robô através de obstáculos para que ele atinja certos
objetivos. Considere que o
robô começa o jogo na posição (0, 0) do plano
cartesiano. O objetivo do robô é chegar até portais que
são casas especiais localizadas em pontos cujo valor da
coordenada y é o dobro da de x, considerando valores
absolutos. Por exemplo, há portais nas casas: (2,
4),(-3, 6),(1, -2), etc. O ponto (0, 0) não é um portal,
pois é o início do jogo.

Para mover o robô, o jogador deve indicar a
direção e um número que representa a quantidade de
unidades de movimento. As direções são indicadas pelas
letras: C (acima), B (abaixo), E (esquerda), D
(direita).  Por exemplo, o comando "C 2" move o robô para cima, duas
unidades. Supondo que este foi o primeiro movimento do
robô, sua nova posição será (0, 2). Se o primeiro
movimento fosse "B 1" ele iria para a posição (0, -1).
Se o primeiro movimento fosse para a esquerda "E 3",
assumiria a posição (-3, 0) e, caso fosse para a direita
"D 5", a posição seria (5, 0).

Construa o programa que controla o jogo "Karel, o robô".

## Entrada

Em cada linha da entrada, é lido um comando de
movimento (C, B, E ou D), seguido de um número inteiro
não-negativo de unidades de movimento.

## Saída

O programa termina quando o robô chega a um portal ou
quando o jogador informa zero para o número de unidades
de movimento. No primeiro caso, deve ser apresentada a
mensagem "Parabéns, conquista do portal (x, y)", onde x
e y são as coordenadas do portal atingido. No segundo
caso, a mensagem a ser apresentada é "Fim de jogo".

## Exemplos de Entrada/Saída

    input: |
    E 1
    B 0
    output: |
    Fim de jogo

    input: |
    D 2
    D 1
    C 3
    C 1
    C 2
    output: |
    Parabéns, conquista do portal (3, 6)