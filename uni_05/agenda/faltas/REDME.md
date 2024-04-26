# Reprovados por Falta

Um professor se cansou de checar manualmente a presença dos alunos. Antigamente,
ele deveria contar todas os registros de presença de cada aluno e gerar um relatório
com a quantidade de faltas. No entanto, a legislação mudou e a pró-reitoria de ensino
estabeleceu que não era necessário especificar a quantidade de faltas para os alunos reprovados por falta.
Ou seja, o professor percebeu que assim que identificasse que o aluno superou o limite de 8 faltas, não
precisaria continuar contando.

Escreva um programa que, dado o registro de presença dos alunos, identifique o número de alunos que foram
reprovados por falta.

# Entrada

O programa deve ler uma sequência de registros de presença (cada linha representa um aluno) e deve imprimir
a quantidade de alunos reprovados por falta.

A leitura é encerrada pelo caractere '-'.

# Saída

Na saída, seu programa deve imprimir a quantidade de alunos reprovados por falta.


## Exemplo

    python joao.py
    ......f.....f.
    ffffffffffffff
    ......f.....f.
    ..ffffffff..f.
    -
    2 aluno(s) reprovado(s) por falta.

# Importante!

    Não é permitido utilizar o comando **for**.