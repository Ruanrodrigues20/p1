# Inverte Dicionário

Escreva a função `inverte_dicionario(dicionario)` que recebe um dicionário e
retorna o dicionário inverso. No dicionário inverso, as chaves
são os valores do dicionário original, enquanto os valores
são as chaves do dicionário original. Note que os valores do dicionário invertido
devem ser armazenados em lista ordenada, uma vez que pode, no dicionário original,
os valores podem ser repetidos. Veja os exemplos abaixo para entender melhor
o funcionamento da função.


# Exemplo de asserts

```
m = {"a": 2, "b": 3, "c": 2}
assert inverte_dicionario(m) == { 2: ["a", "c"], 3: ["b"] }
```


# Restrições

Você não deve usar nenhuma função de ordenação de python.
Para ordenar os elementos, use inserção ordenada.
