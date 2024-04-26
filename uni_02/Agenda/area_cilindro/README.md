# Área do Cilindro

Um estudante de ensimo médio precisa escrever um
pequeno programa interativo para calcular a
superfície de um
cilindro. Pede-se que você escreva o programa de acordo
com sua especificação.

## Entrada

Ao funcionar, o programa lê da entrada o diâmetro do
cilindro e sua altura.

## Saída

Na saída, além dos prompts para ler os dados do
usuário, o programa imprime na saída a superfície
total do cilindro, de acordo com a formatação dada no
exemplo de execução abaixo.

## Exemplo de execução

A listagem abaixo demonstra como o estudante deseja que
o programa funcione quando estiver corrigido. Observe
que ele digitou na entrada apenas os valores do
diâmetro e da altura cilindro.

    $ python supcilindro.py
    Cálculo da Superfície de um Cilindro
    ---
    Medida do diâmetro? 2.5
    Medida da altura? 6.0
    ---
    Área calculada: 56.94

## Como se calcula a área de um cilindro

Relembre que a área de um cilindro se calcula,
somando-se a área das bases à área da lateral. Cada
uma das bases, por serem círculos, têm suas áreas
dadas pelo produto de pi pelo quadrado do raio. A
área da lateral é simplesmente a área de um retângulo
cujos lados são a altura do cilindro e o perímetro da
base. Este, por sua vez, é determinado como sendo o
dobro de pi multiplicado pelo raio.