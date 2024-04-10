# Validação de Triângulos

Para que se possa construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.

Escreva um programa que a partir das medidas dos lados verifica se eles determinam um triângulo válido ou não.

## Entrada

O Programa recebe três medidas, cada uma numa linha separada, que correspondem às medidas dos lados de um triângulo.

## Saída

O programa imprime na saída o resultado da verificação se as medidas dos 3 lados obedecem à condição de existência do triângulo formando um triângulo válido. Em caso afirmativo, imprima "triangulo valido." e o seu perímetro. Caso contrário, imprima "triangulo invalido.".

## Exemplos de Execução

```
$ python3 eh_triangulo.py
2
2
2
triangulo valido. 6
```

```
$ python3 eh_triangulo.py
20
10
5
triangulo invalido.
```