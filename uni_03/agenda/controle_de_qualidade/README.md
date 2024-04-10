# Controle de Qualidade

Uma das reclamações mais frequentes de clientes de supermercados é o fato de haver muita água em congelados e, por consequência, o custo do produto não se mostra justo.  Para verificar o problema, o PROCON designou uma equipe de controle de qualidade para verificar a porcentagem de água no peso total do produto. A tolerância, segundo a lei estabelecida, é 10%. Isto é, se menos de 10% do peso de uma carne congelada for de água, o produto é considerado "em conformidade". Ainda, se a % de água for menor que 5%, o produto ganha um selo especial de qualidade (Produto Qualis A). Caso contrário, o produto é considerado como "não conforme".

Escreva um programa que leia o peso (em kg) do produto antes de depois de descongelar e classifica o produto de acordo com as regras acima.

## Entrada

O programa deve ler de duas linhas da entrada o peso do produto antes e depois de descongelar.

## Saída

Na saída, o programa indica que percentagem do produto é de água congelada e classifica o produto em

- `Produto não conforme`
- `Produto em conformidade` ou
- `Produto qualis A`.

## Exemplos de execução

```
$ python3 solucao.py
4.5
1.0
77.8% do peso do produto é de água congelada.
Produto não conforme.
```

```
$ python3 solucao.py
10.0
9.8
2.0% do peso do produto é de água congelada.
Produto qualis A.
```

```
$ python3 solucao.py
10.0
9.3
7.0% do peso do produto é de água congelada.
Produto em conformidade.
```