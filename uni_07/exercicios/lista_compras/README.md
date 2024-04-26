# Lista de Compras

Um apliativo de lista de compras contém uma sequências de
itens em ordem alfabética. Pede-se que você escreva a função
com efeito colateral `adiciona_item(item, lista)` que adiciona
item à lista, mas que a mantém em ordem alfabética.

# Importante

A função não deve usar qualquer algoritmo ou função de ordenação.

Para aumentar a lista só é permitido usar *append*.

# Exemplo de uso da função

```
lista = ['acucar', 'leite', 'paes', 'queijo']
adiciona_item('cafe', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
```