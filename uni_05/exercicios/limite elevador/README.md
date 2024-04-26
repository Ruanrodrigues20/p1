# Acima do Limite do Elevador

Um operador de elevador, além de escolher o andar para qual o elevador deve
partir, possui uma outra responsabilidade -- checar se a razão entre crianças
e adultos está de acordo com a norma e se o peso não ultrapassa o limite de
700.00 kg. Nesse caso, a razão entre crianças e adultos é considerada de
extrema importância e deve ser checada antes do peso total.

O elevador parte assim que a configuração de pessoas não respeita um
dos dois critérios estabelecidos acima.

Faça um programa que leia da entrada a razão máxima permitida entre crianças
e adultos e em seguida leia os dados das pessoas que querem entrar no
elevador. Seu programa deve parar quando um dos critérios não for respeitado
e deve imprimir uma mensagem com a configuração do elevador após a saída.
Note que essa configuração não pode incluir a pessoa que fez com que um
dos critérios não fosse verdadeiro.

# Entrada

A entrada consiste em: i) um número decimal que define a razão máxima entre
o número de crianças e adultos (e. g. 0.5 significa que o máximo permitido
é uma criança para cada dois adultos) e ii) uma sequencia de linhas que
estabelecem o tipo da pessoa (*c* para crianças e *a* para adultos) e o
seu peso, respectivamente.

# Saída

Na saída seu programa deve imprimir as seguintes mensagens:

    Limite atingido.
    Elevador saiu com X pessoas e Y kg.

Obs: X e Y são variáveis de acordo com a entrada.

## Exemplos de execução

    $ python joao.py
    0.5
    a 100.00
    a 50.00
    c 10.00
    c 2.00
    Limite atingido.
    Elevador saiu com 3 pessoas e 160.00 kg.

    $ python joao.py
    1
    c 150.00
    Limite atingido.
    Elevador saiu com 0 pessoas e 0.00 kg.

    $ python joao.py
    0.7
    a 160.32
    a 30.89
    a 69.90
    c 78.90
    a 120.80
    a 300.00
    Limite atingido.
    Elevador saiu com 5 pessoas e 460.81 kg.