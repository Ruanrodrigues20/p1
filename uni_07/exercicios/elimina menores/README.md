# Elimina Menores

Escreva a função `elimina_menores(num, lista)` que recebe um
número inteiro e uma lista de inteiros. A função deve
eliminar da lista todos os valores menores que num. Ainda
deve retornar o número de elementos removidos.Veja os
asserts abaixo:

## Exemplos de asserts

```
lista1 = [100,200,300,400]
assert elimina_menores(100, lista1) == 0
assert lista1 == [100,200,300,400]

lista2 = [3,5,1,7,10,9]
assert elimina_menores(4, lista2) == 2
assert lista2 == [5,7,10,9]
```
