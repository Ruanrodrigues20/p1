Um construtor precisa calcular quantas caixas de
cerâmica deve comprar para revestir cozinhas e
banheiros. Para isso, ele pede que você escreva um
programa que dadas as dimensões do vão (comprimento,
largura e altura), calcule a quantidade de caixas de
cerâmica necessárias para cobrir as paredes e o chão do
ambiente. Áreas de janelas podem ser completamente
desconsideradas por seu programa.

# Entrada

Seu programa deve ler da entrada a capacidade de
revestimento de cada caixa de cerâmica e as dimensões
(em metros) do vão.

# Saída

O programa deve escrever na saída a área total que deve
ser coberta, correspondente à soma das áreas do chão e
das paredes, mas sem incluir a área do teto. Também
deve produzir na saída o número de caixas que é
necessário comprar para cobrir o vão em questão.

Considere que o vão tem a forma de um paralelepípedo e
que, portanto, as áreas das paredes e do chão são
calculadas como áreas de retângulos.

# Exemplo de execução

Ao ser executado, o programa deve executar como
mostra a listagem abaixo.

    $ python dalton.py
    Capacidade de revestimento? 1.5

    == Dados do vão a revestir ==
    Comprimento? 3.0
    Largura? 3.0
    Altura? 2.5

    == Resultados ==
    Área total a revestir: 39.0 m2
    Número de caixas: 26
    $ _