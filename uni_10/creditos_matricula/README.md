# Crédito Matrícula

Na UFCG, as disciplinas de todos os cursos são de resposabilidade das unidades
acadêmicas. Nesse caso, cada unidade acadêmica é responsável por um conjunto
de disciplinas que são ministradas tanto para os alunos vinculados aos cursos
da unidade quanto para alunos de outros cursos vinculados a outras unidades acadêmicas.
Por exemplo: alunos do curso de Ciência da Computação, curso vinculado à Unidade
Acadêmica de Sistemas de Computação (UASC), podem se matricular em Cálculo I, que
é de responsabilidade da Unidade Acadêmica de Matemática (UAM).

Pede-se que você escreva a função `num_creditos(bd_ufcg, matricula)` que recebe como
parâmetro as informações da universidade (unidades acadêmicas, disciplinas e
alunos matriculados) e a matrícula do aluno e retorna a quantidade de créditos em que
o aluno está matriculado.

Considere que as informações da universidade são armazenadas num mapa cujas chaves
são as unidades acadêmicas e os valores associados são também mapas que, por sua vez,
contêm como chave uma tupla contendo o nome da disciplina e o respectivo crédito
e o valor associado é uma lista contendo o número de matrículas dos alunos matriculados
na discplina. Veja os asserts para compreender melhor a semântica da função.

## Exemplo de assert

```
bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"],
          ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
          "UAF": {("Física Clássica", 4): ["11624200"],
          ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
          "UAM": {("Cálculo I", 4): ["11624100", "11624300"],
          ("Álgebra Linear", 4): ["11624300"]}
               }

assert num_creditos(bd_ufcg, "11624100") == 8
```
