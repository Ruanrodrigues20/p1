# Sismógrafo

Um sismógrafo é um dispositivo que detecta e registra as vibrações
(sismos) da Terra, sejam elas provocadas por processos naturais ou
pelo homem. São bastante usados na identificação de terremotos.
Em geral, utilizam uma grandeza definida pela **Escala Richter**
que, em teoria, varia de zero a infinito. Apesar dessa escala
infinita, nunca se registrou até hoje um terremoto com magnitude
maior do que 10 graus na escala Richter.

Um novo modelo de sismógrafo está sendo instalado em uma área que
apresenta muitos sismos e ele deve registrar periodicamente o
valor da magnitude dos sismos e recalcular a magnitude média dos
sismos registrados para ajudar no estudo da variabilidade dos
sismos, contribuindo também na calibração do novo modelo de sismógrafo.
Além disso, como o sismógrafo foi concebido a partir de dados
históricos, ele é feito para alertar que o sistema atinja sismos de
magnitude muito altas. Assim, o sismógrafo deve emitir
um alerta e interromper os registros assim que um sismo tenha
ultrapassado o limite de segurança estabelecido (10 pontos na
escala Richter).

Escreva um programa que vai funcionar de forma  _interativa_ que trata
os dados recebidos do sismógrafo. O programa deve ler medições
de sismos, deve manter e mostrar as medições lidas e a média
das medições e deve interromper as medições tão logo a medida
ultrapasse o limite estabelecido de 10 pontos na escala Richter.

## Entrada

A entrada do programa consiste em uma sequência de N > 0
medições de sismos produzidos pelo sismógrafo. Por ser um dispositivo
físico, a sequência é, em princípio, de tamanho ilimitado. Aqui
isso significa que seu programa deve ler apenas certo número de
linhas da entrada e ignorar as demais. Veja abaixo, um exemplo de
entrada válido para o programa. Observe que o sismógrafo em certo
momento vai além do valor de 10 pontos da escala Richter  estabelecido.
Isso significa que todos os dados a partir daquele momento podem ser
ignorados, já que o programa deve concluir o processamento e emitir o
alerta.

```
8.0
8.5
9.1
9.6
9.9
10.3
10.6
4.9
4.6
```

# Saída

A saída do programa contém uma linha para cada medição lida
abaixo do limite de segurança. E duas linhas adicionais se/quando
esse limite for atingido, para emitir o alerta e para indicar
quantas medições foram feitas até o momento do alerta. A listagem
abaixo mostra uma saída válida correspondente à entrada acima.

> Observe bem a formatação dos dados na saída. Todos os valores
> das medições devem ser formatados com uma casa decimal.

```
m = 8.0 (média = 8.0)
m = 8.5 (média = 8.2)
m = 9.1 (média = 8.5)
m = 9.6 (média = 8.8)
m = 9.9 (média = 9.0)
m = 10.3 (média = 9.2)
ALERTA: limite de sismo atingido!
número de medições: 6
```

# Exemplo

O programa é interativo, logo, espera-se que as saídas ocorram
de forma contínua à medida que os dados são lidos da entrada.
Isso significa que ao executar o programa, os dados de entrada e
de saída poderão ser vistos de forma intercalada.

> Neste caso, os dados de entrada produzidos depois do limite ter
> sido atingido não serão visualizados apropriadamente, porque o
> processo não os irá ler. Por isso, a listagem abaixo não terá
> os dados de leitura após o limite ter sido atingido.

```
$ python sismo.py
8.0
m = 8.0 (média = 8.0)
8.5
m = 8.5 (média = 8.2)
9.1
m = 9.1 (média = 8.5)
9.6
m = 9.6 (média = 8.8)
9.9
m = 9.9 (média = 9.0)
10.3
m = 10.3 (média = 9.2)
ALERTA: limite de sismo atingido!
número de medições: 6
```



