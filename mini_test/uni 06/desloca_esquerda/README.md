# Desloca o elemento para a esquerda

Implemente a função `desloca(lista, origem, destino)` que move o elemento na
posição **origem** para a posição **destino** recebidas como argumento.

Assuma que **origem** e **destino** são índices válidos e **origem** sempre é maior
do que **destino**. Isto é, o deslocamento é para a esquerda.

Note também que não basta apenas trocar **origem** por **destino**, é preciso
deslocar os elementos entre essas duas posições. Veja os exemplos de asserts
para melhor entendimento da questão.

A função tem efeito colateral e **não é permitido** criar outra lista.

## Exemplos de assert

```
l1 = [2,6,9,11,13,5]
assert desloca(l1, 4, 2) == None
assert l1 == [2,6,13,9,11,5]

l1 = [0,1,2,3,4,5,6]
assert desloca(l1, 6, 4) == None
assert l1 == [0,1,2,3,6,4,5]
```ca