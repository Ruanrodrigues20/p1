# Formata CPF

Um supermercado sorteou 3 clientes para receberem como prêmio um ano de feira grátis. Esses
clientes são identificados pelo CPF, um número de 11 dígitos (ex: 82107342569). Contudo,
para apresentar os ganhadores, o programa de sorteio deve formatar o CPF da maneira como
estamos acostumados, isto é, com um hífen antes dos dois últimos dígitos (ex: 821073425-69).
Além disso, para fins de verificação, o programa deve imprimir a soma dos dois
últimos dígitos dos CPFs lidos.

Implemente um programa que leia *como inteiro* o CPF dos vencedores e imprima esses CPFs
com a formatação discutida acima, além da soma dos dois últimos dígitos de cada CPF.

Para fins de simplificação você pode assumir que o dígito 0 não aparece em nenhum dos cpfs.

## Entrada

Seu programa deve ler da entrada padrão os 3 CPFs dos clientes sorteados. Esses CPFs devem, obrigatoriamente,
serem lidos como inteiros.

## Saída

Seu programa deve imprimir os CPFs na formatação padrão, além de imprimir a soma dos dois últimos dígitos
de cada CPF.

## Exemplo de execução

    python solution.py
    93623421869
    99999999999
    11111111111
    936234218-69
    15
    999999999-99
    18
    111111111-11
    2


## Restrições

**Não é permitido usar *str()**. Você deve ler os CPFs como inteiro e usar operações matemáticas
para separar os 9 primeiros dígitos dos dois últimos.