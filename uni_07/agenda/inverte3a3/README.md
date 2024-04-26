# Sequencia Invertida 3 a 3

Escreva a função `inverte3a3(s)` que recebe uma _string_
`s` de caracteres e retorna uma _string_ que corresponde à
_inversão 3 a 3_ dos caracteres de `s`.

A chamada _inversão 3 a 3_ consiste em inverter a ordem dos
_tokens_ (pedaços) de `s` de tamanho 3. Assim, por exemplo, se
`s` for `abcdef` a _string_ retornada deve ser `defabc`, porque
os tokens `abc` e `def` são invertidas. Outro exemplo seria
`abcdefghijkl` que resultaria em `jklghidefabc`. Perceba que o _token_
`abc` que era o primeiro de `s` é o último na _string_
resultante. E que `cde`, que era o segundo, se torna o penúltimo
(ou segundo de trás pra frente) na _string_ resultante.

## Detalhes e restrições

1. Você pode assumir que a _string_ `s` tem tamanho múltiplo de 3.
2. Você não deve utilizar _slices_.

## Exemplo

```python
assert inverte3a3("abcdef") == "defabc"
```