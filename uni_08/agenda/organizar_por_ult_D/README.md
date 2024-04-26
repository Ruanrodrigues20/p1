# Organiza por último dígito

Um banco utiliza um critério próprio para organizar os seus
clientes na fila de espera. De tempos em tempos, um funcionário
passa pela fila movendo os clientes _prioritários_ para a frente
dos demais clientes. Um cliente é dito prioritário se seu número
de conta termina em um dígito menor ou igual a 5.

O processo do funcionário para reorganizar a fila consiste em
identificar cliente por cliente, começando pelo início da fila,
quais clientes são prioritários. Cada vez que um cliente
prioritário é encontrado, ele é movido para a frente na fila, até
ficar na frente de todos os clientes não prioritários e atrás de
todos os clientes prioritários que tiverem chegado antes. Dessa
forma, se houver mais de um cliente prioritário, eles serão
atendidos por ordem de chegada. E os clientes não prioritários
serão atendidos depois dos privilegiados, mas por ordem de
chegada entre eles.

Por exemplo, considere que a fila tem as contas de números.

3819, 3318, 2977, 4331, 2282 e 1016

O funcionário, então, iniciará relocando o cliente 4331. Ele será
colocado à frente de todos os clientes à frente deles, porque ele
é o primeiro prioritário. Logo, após essa etapa a fila ficará
sendo:

4331, 3819, 3318, 2977, 2282 e 1016

O segundo cliente a ser movido será o 2282. Após sua relocação, a
fila será:

4331, 2282, 3819, 3318, 2977 e 1016

Como não há mais clientes prioritários, esse será o estado final
da fila.

## A função

Implemente a função `organiza_por_ultimo_digito(contas)` que,
dado um array com o número das contas dos clientes na ordem de
chegada, **altere** o array aplicando a regra definida acima.

> **ATENÇÃO** Embora a função receba uma lista Python, você
> deve tratá-la como um array. Logo, as operações possíveis
> devem se restringir à API de arrays.

# Exemplo de uso da função

Leia os testes fornecidos e confira a semântica da função.

