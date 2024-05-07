# Submatriz

Escreva a função `submatriz(A, p, q, r, s)` que recebe a
amatriz A (m x n) e retorna uma submatriz contendo o bloco
de dados delimitado pelos índices `p` e `q` (canto superior
esquerdo) e `r` e `s` (canto inferior direito).

## Condição de existência

Para que a submatriz especificada esteja bem definida é
necessário que todos os índices (`p`, `q`, `r` e `s`) sejam
válidos para a matriz recebida e ainda que `p <= r <= m`, que
`q <= s <= n`. Caso isso não ocorra, a submatriz não está
definida.

## Especificação da função

Se a submatriz especificada for bem definida a função deve
retornar uma matriz que a represente. Caso contrário, a
função deve retornar `None`. Em qualquer caso, a função não
deve ter qualquer efeito sobre a matriz original. Veja os
asserts no exemplo abaixo.

Leia o arquivo de teste para ver um `assert` que exemplifica o
uso da função.