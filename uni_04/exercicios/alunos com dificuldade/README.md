# Alunos com dificuldade

Um professor quer identificar quais de seus alunos estão com mais
dificuldades na disciplina. Para isso, decidiu que precisa usar
um pequeno programa que leia os dados que tem e que imprima uma
lista dos alunos que estão com média abaixo da média da turma.

## Entrada

A entrada consiste em duas linhas de dados apenas. Na primeira
linha são indicados os identificadores dos N > 0 alunos,
separados por um espaço em branco. Na segunda linha são
fornecidas todas as notas da turma, sendo exatamente duas notas
para cada aluno. A ordem das notas nas segunda linha corresponde
exatamente à ordem dos identificadores na primeira.

```
Ana Beatriz Carla Daniel Eduardo Flavio
7 9 8 10 6.5 4 7 8.5 3 7 0 0
```

## Saída

A saída do programa consiste em um relatório contendo a listagem
dos alunos abaixo da média da turma, sendo um aluno por linha. Em
cada linha devem constar as duas notas do aluno, sua média e seu
identificador, formatados como mostra o exemplo abaixo (com 1
ponto decimal). Na última linha do relatório deve ser indicado o
valor da média da turma, formatado como indica o exemplo abaixo
(que corresponde à entrada acima).

```
- 6.5 4.0 (5.2) Carla
- 3.0 7.0 (5.0) Eduardo
- 0.0 0.0 (0.0) Flavio
> media turma: 5.83
```