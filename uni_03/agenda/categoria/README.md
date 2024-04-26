# Categorias

Escreva um programa que com base na idade de um nadador determina em que categoria ele irá competir. A indicação da categoria é definida de acordo com as regras que seguem:

1. Infantil A - 5 a 7 anos
2. Infantil B - 8 a 10 anos
3. Juvenil A - 11 a 13 anos
4. Juvenil B - 14 a 17 anos
5. Senior - Acima de 17 anos

## Entrada

O programa recebe na primeira e segunda linha da entrada o nome e a idade do nadador, respectivamente.

## Saída

Na saída, deve imprimir o nome, a idade e a categoria a que o nadador pertence na competição.

## Atenção

O programa só recebe números inteiros maiores do que 0 para representar a idade. Caso o nadador tenha menos do que 5 anos, o programa informa "Não pode competir.".  Veja os exemplos de entrada e saída.

## Exemplos de Execução

```
$ python3 categoria.py
Antônio
5
Antônio, 5 anos, Infantil A.
```

```
$ python3 categoria.py
André
9
André, 9 anos, Infantil B.
```

```
$ python3 categoria.py
Eduardo
3
Eduardo, 3 anos, Não pode competir.
```