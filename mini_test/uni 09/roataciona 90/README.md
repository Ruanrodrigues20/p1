# Rotaciona 90 Graus

Um programa de tratamento de imagens requer que seja criada a
função `rotaciona90(imagem)` que cria uma nova imagem
semelhante à original, mas rotacionada em 90 graus.

Por simplicidade, assumamos que a imagem é composta por uma
matriz de inteiros (na prática, são tuplas de inteiros).
Assim, se a imagem for, por exemplo:

```
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
```

A imagem rotacionada em 90 graus (à direita) seria dada pela
matriz:

```
4 3 2 1
5 4 3 2
6 5 4 3
7 6 5 4
8 7 6 5
```

Pede-se que você construa uma função que faça essa rotação.

# Exemplo de assert

```
I = [[1, 2, 3, 4, 5],
     [2, 3, 4, 5, 6],
     [3, 4, 5, 6, 7],
     [4, 5, 6, 7, 8]]

R = rotaciona90(I)
assert R == [[4, 3, 2, 1],
             [5, 4, 3, 2],
             [6, 5, 4, 3],
             [7, 6, 5, 4],
             [8, 7, 6, 5]]
```