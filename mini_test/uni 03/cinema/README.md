# Entrada no Cinema

Em um cinema, decide-se instalar um software para regular a entrada de crianças
para certos filmes. O usuário deve informar o ano atual e o ano de nascimento
da pessoa e, em alguns casos, deve ainda informar se a criança está acompanhada
dos pais ou não.

Pessoas com 16 anos ou mais podem entrar no filme livremente. Crianças com menos
16 e a partir de 14 anos podem entrar, desde que acompanhadas dos pais. E
crianças com menos de 14 anos não podem entrar de forma alguma. Pede-se que você
escreva o programa para regular a entrada no cinema.

## Entrada

A primeira linha da entrada consiste em um valor inteiro que indica o ano atual.
A segunda linha da entrada consiste em outro valor inteiro que representa o ano
de nascimento da criança. Haverá mais uma linha na entrada apenas se a criança
tiver 14 ou 15 anos, sendo um único caractere que indica se a criança
está ou não acompanhada dos pais (`s` para indicar _sim_ ou `n` para indicar
_não_). Veja abaixo um exemplo de entrada válida.

```
Ano atual? 2021
Ano de nascimento? 2006
Com os pais? n
```

## Saída

A saída consiste em duas linhas: a primeira apresenta uma mensagem indicando a
idade calculada da pessoa e a segunda informa a orientação em relação à entrada
da pessoa. As mensagens possíveis para a segunda linha são:

1. "`Entrada permitida`"
2. "`Entrada proibida para menores de 14 anos`"
3. "`Entrada proibida para menores de 16 anos sem os pais`"

Considerando o exemplo de entrada apresentado anteriormente, a saída seria a
seguinte.

```
Idade calculada: 15 anos
Entrada proibida para menores de 16 anos sem os pais
```

## Exemplos de execução

### Exemplo 1

```
$ python exemplo.py
Ano atual? 2021
Ano de nascimento? 2006
Idade calculada: 15 anos
Com os pais? n
Entrada proibida para menores de 16 anos sem os pais
```

### Exemplo 2

```
$ python exemplo.py
Ano atual? 2021
Ano de nascimento? 2011
Idade calculada: 10 anos
Entrada proibida para menores de 14 anos
```