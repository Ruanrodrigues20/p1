# Subtração de Polinomios

Um software matemático representa polinômios de uma única variável através de listas que contêm os coeficientes em ordem crescente de grau. Por exemplo, o polinômio p1(x) = 3x2 + 4x - 5 é representado pela lista [-5, 4, 3], indicando que os coeficientes são -5, 4 e 3, para os monômios de grau 0, 1 e 2, respectivamente. O polinômio p2(x) = 5x6 + 2x2 - 1 é representado pela lista [-1, 0, 2, 0, 0, 0, 5], dado que os coeficientes de grau 1, 3, 4 e 5 são iguais a zero.

Pede-se que você escreva a função `subtrai_polinomios(p1, p2)` sem efeito colateral que retorna a lista que representa o polinômio resultante da subtração do polinômio p2 de p1, ou p1 - p2. A função deve retornar a representação reduzida do polinômio, isto é, sem os coeficientes zero desnecessários (veja o exemplo).

Relembre que os coeficientes do polinômio diferença são dados pela diferença dos coeficientes de mesmo grau dos polinômios sendo subtraídos. Assim, p1 - p2, no exemplo acima seria igual a -5x6 + x2 + 4x -4.

## Exemplos e Asserts

Veja o arquivo de testes fornecido.

<small>Dalton Serey</small>