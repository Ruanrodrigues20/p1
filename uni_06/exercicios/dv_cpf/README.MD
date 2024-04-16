# Dígitos de Verificação do CPF

Escreva a função `calcula_digitos_verificacao(cpf)` que calcula e retorna os
dois dígitos de verificação de um número de CPF. Para o cálculo do primeiro
dígito verificador, os dígitos do número original, começando da direita para a
esquerda (do menos significativo para o mais significativo) são multiplicados,
respectivamente, por 2, por 3, por 4, e assim sucessivamente, até chegar ao
primeiro dígito do número. O somatório final desses produtos deve ser
multiplicado por 10 e dividido por 11. O resto da divisão (módulo 11) será o
primeiro dígito verificador. Para calcular o segundo dígito, considera-se o
primeiro dígito como parte do número e se efetua exatamente o mesmo processo.

> IMPORTANTE: Se uma das expressões dos dígitos verificadores resultar em 10, o
> dígito efetivo será 0 (zero).

## Entrada

A função deve receber uma _string_ de nove dígitos como parâmetro de entrada.

## Saída

A função deve retornar uma _string_ com os dois dígitos de verificação
calculados de acordo com a regra de formação especificada acima.

## Exemplo

Suponha que o número principal do CPF seja `153245875`. O primeiro dígito de
verificação será calculado pela expressão abaixo, cujo resultado é 4:

```
10 * (5 * 2 + 7 * 3 + 8 * 4 + 5 * 5 + 4 * 6 + 2 * 7 + 3 * 8 + 5 * 9 + 1 * 10) mod 11
```

E o segundo dígito é 0, obtido através da expressão:


```
10 * (4 * 2 + 5 * 3 + 7 * 4 + 8 * 5 + 5 * 6 + 4 * 7 + 2 * 8 + 3 * 9 + 5 * 10 + 1 * 11) mod 11
```


## Exemplo de assert

A função deve retornar os digitos de verificação como um _string_.

```
assert calcula_digitos_verificacao('153245875') == '40'
```