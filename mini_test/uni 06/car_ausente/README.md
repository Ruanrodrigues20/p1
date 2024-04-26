# Caractere Ausente

Considere duas sequências de caracteres quaisquer, uma contendo n caracteres
e outra contendo n+1 caracteres. As sequências contêm exatamente os mesmos
caracteres, exceto por um único caractere a mais em uma das sequências, ou seja,
um único caratere diferencia estas sequências.

Escreva a função `caractere_ausente(seq1, seq2)` que compara as duas sequências
e retorna qual caractere está faltando em uma das sequências.

Considere que apenas letras minúsculas e sem acentos estão presentes nas sequências.
Além disso, não há repetição de caracteres e a ordem dos caracteres não importa na sequência.

## Exemplo 1

```
seq1 = "computer"
seq2 = "compter"
assert caractere_ausente(seq1, seq2) == "u"
```

## Exemplo2

```
seq1 = "dolate"
seq2 = "teclado"
assert caractere_ausente(seq1, seq2) == "c"