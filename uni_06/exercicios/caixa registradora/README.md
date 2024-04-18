# Caixa Registradora

Para manter o controle do fluxo de caixa de um comércio é necessário anotar cada venda realizada e fechar o caixa no fim do dia com todos
os valores anotados coincidindo com o valor encontrado no caixa. você deve criar uma função para facilitar o cálculo de caixa. Sua função
deve receber como parâmetros uma lista de valores reais representando as vendas e um número real que representa a meta. Como resultado,
sua função deve retornar outra lista com um relatório geral sobre o dia contendo a soma das vendas do dia, o total de comissões e a
situação (lucro ou prejuízo). Considere que:

- Cada venda abaixo de R$ 1.000,00 paga ao vendedor uma comissão de 5%;
- Vendas com valores iguais ou superiores a R$ 1.000,00 e menores que R$ 5.000,00 geram comissões de 10%;
- Vendas com valores iguais ou superiores a R$ 5.000,00 geram comissões de 15%;
- A soma das vendas do dia, diminuídas as comissões, deve ser superior ou igual à meta para dar lucro à loja;
- Soma das vendas do dia inferior à meta gera prejuízo.

## Entrada
A função deve ler uma lista de números reais, contendo cada venda realizada no dia e um número real que representa a meta desejada para aquele dia.

## Saída
A função deve retornar uma lista que servirá como relatório do dia, ela deve conter:

- A soma de todas as vendas do dia;
- O valor total pago em comissões;
- Uma string relatando a situação do dia ("Lucro" ou "Prejuizo").

## Exemplo de assert

```
assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
```