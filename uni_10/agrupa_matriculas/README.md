# Agrupa Matrículas

Os primeiros 3 dígitos da matrícula de uma universidade
indicam o período de ingresso do estudante. Pede-se que você
escreva uma função que dados os estudantes matriculados em
uma turma, contabilize quantos estudantes há de cada
período. Escreva a função `agrupa_por_periodo(alunos)` que
recebe uma lista de matrículas de estudantes matriculados em
uma turma e que retorna um mapa cujas chaves são strings
correspondendo aos períodos e cujos valores são o total de
estudantes daquele período matriculados.

# Exemplo de asserts


```
turma = [
  '0511114', '0521137', '0611001',
  '0611003', '0611004', '0621006',
  '0811007', '0811009', '0811502',
  '0811604', '0811605',
]
assert agrupa_por_periodo(turma) == {
        '051': 1,
        '052': 1,
        '061': 3,
        '062': 1,
        '081': 5,
}
```