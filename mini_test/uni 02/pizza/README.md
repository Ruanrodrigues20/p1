# Reunião Pizza

Em uma reunião de amigos decidiu-se organizar um lanche no final.
Como a maioria escolheu comprar pizzas, você deve criar um programa
para facilitar a divisão de fatias e calcular o custo. Todos devem
ficar com uma quantidade igual de fatias. Todas as pizzas possuem 8
fatias e mesmo valor. Assuma que a reunião tem pelo menos
uma pessoa.

## Entrada

A entrada do programa consiste em três linhas, sendo as duas primeiras
contendo valores inteiros e a última contendo um valor float. A primeira
linha indica o número de amigos presentes na reunião. A segunda linha
representa a quantidade de pizzas compradas e a última apresenta o preço
de uma pizza.

```
9
4
32.5
```

## Saída

A saída apresenta duas linhas, em que a primeira deve mostrar a quantidade
de fatias que cada amigo poderá comer e também a quantidade de fatias que
sobraram após a divisão. A última linha mostra o valor total pago. Observe
abaixo um exemplo de como deve ser a saída.

```
3 fatia(s) para cada um e sobra(m) 5 fatia(s)
Valor total: R$ 130.00
```

## Exemplo de execução

```
$ python reuniao_pizza.py
9
4
32.5
3 fatia(s) para cada um e sobra(m) 5 fatia(s)
Valor total: R$ 130.00
```