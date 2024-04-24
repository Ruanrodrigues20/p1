# Fila de Atendimento de Pacientes

Em um consultório médico, os pacientes que vão chegando entram em
uma fila única para a espera de atendimento. Dependendo do dia,
podem atender neste consultório, até `n` médicos. Pede-se que
você escreva a função `filas_de_atendimento(fila_unica, n)` cujo
propósito é distribuir os pacientes em filas para cada um dos
médicos. A ordem de chegada dos pacientes deve ser preservada.

Para distribuir os pacientes nas filas de cada médico deve-se
pegar, em ordem de chegada na fila única, um paciente para cada
fila de médico e repetir o processo até terminar a fila única.

O primeiro parâmetro passado para a função é a fila dos pacientes
por ordem de chegada. O segundo parâmetro, refere-se ao
número de médicos que estão atendendo na clínica. Você pode
assumir que
há pelo menos um médico (`n` > 0). A função deve retornar uma
lista com as filas formadas para cada um dos médicos. É
importante que se houver filas vazias, elas devem ser retornadas
normalmente.

## Exemplos e Asserts

```
pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
assert filas_de_atendimento(pacientes, 3) == [
    ['Andre', 'Carlos'],
    ['Antonio', 'Claudia'],
    ['Bianca']
]

pacientes = ['Andre', 'Antonio', 'Bianca', 'Carlos']
assert filas_de_atendimento(pacientes, 2) == [
    ['Andre', 'Bianca'],
    ['Antonio', 'Carlos']
]
```