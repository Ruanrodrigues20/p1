# Componentes na esteira

Na linha de produção de uma fábrica, os engenheiros se preocupam com duas
coisas: 1) que os componentes necessários estejam presentes na esteira; e 2)
que a ordem em que os componentes apareçam na esteira seja a esperada.

Pede-se que você escreva a função `verifica_esteira(esteira, componentes)` que
recebe: i) uma lista `esteira` contendo os identificadores inteiros de todos os
componentes presentes na esteira; e ii) a lista `componentes` que contém os
identificadores dos componentes na ordem em que se espera que apareçam na
esteira. A função deve retornar `True` se todos os elementos especificados em
`componentes` estão presentes na lista `esteira`, na ordem indicada. E deve
retornar `False` caso contrário.

Por exemplo, se esteira contiver os componentes 2, 1, 3 e 4, a
lista `esteira` será igual a `[2, 1, 3, 4]`. Se os componentes
esperados são o `2` e `3`, nessa ordem, a lista `componentes`
deve ser `[2, 3]` e, nesse caso, a função deve retornar `True`
porque os componentes estão na esteira na ordem especificada
(embora haja um componente entre os dois). Se os componentes são
o `4`, o `1` e o `3` nessa ordem, isso será indicado pela lista
`componentes` igual a `[4, 1, 3]`.  Neste caso, a função deve
retornar `False` porque, embora os componentes estejam na
esteira, eles não estão na ordem esperada.


## Restrições de implementação

1. A função não deve usar o operador `in`
2. A função não deve ter efeito colateral

> Dica: se você quiser usar o operador `in`, você pode usá-lo numa primeira
> tentativa, mas lembre-se de substituí-lo por uma função que faça o
> equivalente.


## Exemplos e Asserts

```python
esteira = [2, 1, 3, 4]
componentes = [2, 4]
assert verifica_esteira(esteira, componentes)
assert esteira == [2, 1, 3, 4]
assert componentes == [2, 4]
```

```python
esteira = [1, 3, 4]
componentes = [4, 1, 3]
assert not verifica_esteira(esteira, componentes)
assert esteira == [1, 3, 4]
```