# Caixa Preta

Na análise dos dados de uma caixa preta é muito importante
detectar o momento em que houve falha na coleta de dados do
peso, combustível e altitude. Se qualquer um desses elementos
for negativo, considera-se que _a partir daquele momento_
(incluindo o dado negativo) as medições não são mais
confiáveis e que, embora a leitura física dos dados continue,
os valores não devem mais ser considerados na análise.

Faça um programa que leia várias medições de peso,
combustível e altitude e determine o momento em que os dados
passaram a ser considerados inválidos, além de determinar
quantos dados válidos foram lidos.

## Entrada

Seu programa deverá ler na primeira linha um valor N relativo
à quantidade de medições a serem lidas. Depois, seu programa
deverá ler N linhas contendo as medições. Em cada linha, o
peso, combustível e altitude estão separados por espaço.

## Saída

Na saída, seu programa deve imprimir uma mesagem detalhando
qual dado foi considerado inválido, e a quantidade de dados
válidos lidos. Dependendo do dado inválido, a mensagem pode
variar. Veja as três mensagens possíveis abaixo:

- `dado inconsistente. peso negativo.`
- `dado inconsistente. combustível negativo.`
- `dado inconsistente. altitude negativa.`

Além disso, a saída deve especificar quantos dados foram
considerados válidos. Veja um exemplo:

- `7 dados válidos.`

Se nenhum dado inválido for lido, apenas imprima a mensagem
acima referente à quantidade de dados válidos lida.

## Restrições e Recursos permitidos

É permitido utilizar a função `split`. Não é permitido
utilizar a função `map`.

## Exemplo de execução

No exemplo abaixo, observe que o programa imprime a mensagen
indicando um `dado inconsistente` logo após ler o valor
negativo `-1` e indica que é referente a uma `altitude
negativa`. Observe que depois dessa mensagem, outros dados
foram fornecidos ao programa (a linha contendo
`1 1 1` e demais). Ao terminarem os dados, o programa indica
quantos dados válidos foram lidos. Neste caso, houve apenas 5
dados válidos (que foram os valores `10`, `2`, `3`, `3` e
`1`, antes do `-1`).

```
$ python solution.py
5
10 2 3
3 1 -1
dado inconsistente. altitude negativa.
1 1 1
1 -2 1
-2 -3 4
5 dados válidos.
```

Outro exemplo. Neste segundo exemplo, observe que o dado
inconsistente é `-1` referente a um `peso negativo`. Ao
final, o programa indica que apenas `3 dados válidos` foram
lidos, referente aos valores `1`, `2` e `4`, antes do `-1`.

```
python solution.py
3
1 2 4
-1 2 3
dado inconsistente. peso negativo.
1 9 4
3 dados válidos.
```