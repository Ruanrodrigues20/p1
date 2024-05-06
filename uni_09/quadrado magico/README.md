# É Quadrado Mágico?

Escreva uma função que receba uma matriz e verifica se ela representa um quadrado mágico retornando True ou False (booleano).
No quadrado mágico o resultado da soma dos elementos de suas linhas, suas colunas e diagonais tem o mesmo valor. Além disso, não
pode haver elementos repetidos no quadrado.

<img src="http://upload.wikimedia.org/wikipedia/pt/math/2/0/7/207e89a04bf4b5dd7342fe07669a0377.png" alt="quadrado-magico" width="200" height="200" />

## Exemplos de asserts

    quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
    quadrado2 = [[1,2,3],[4,5,6]]
    assert eh_quadrado_magico(quadrado1)
    assert not eh_quadrado_magico(quadrado2)