# Scroll

Em terminais orientados a caracteres é comum que seja necessário
rolar a tela para cima a cada comando dado. Como a tela é
armazenada como uma matriz de caracteres, costuma-se implementar
essa funcionalidade como uma função chamada `scroll` que opera
sobre a matriz. Pede-se que você escreva a função `scroll(m)` que
recebe uma matriz `m` e que a altera movendo todos os seus dados
uma linha acima. Os dados da última linha, contudo, devem ser
todos zerados.


## Exemplo

```
m = [[  1,  2,  3,  4 ],
     [  5,  6,  7,  8 ],
     [  9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ],
     [ 17, 18, 19, 20 ]]

scroll(m)
assert m == [[  5,  6,  7,  8 ],
             [  9, 10, 11, 12 ],
             [ 13, 14, 15, 16 ],
             [ 17, 18, 19, 20 ],
             [  0,  0,  0,  0 ]]
```