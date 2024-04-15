# Campos de Futebol

Um estudante de jornalismo notou que os âncoras dos jornais sempre
utilizam campos de futebol para dar noções de grandes dimensões. Por exemplo,
para anunciar o tamanho da área desmatada na Amazônia no último ano,
o âncora noticiou que foram 8 campos de futebol, ao invés de noticiar 32000.0 m2.

Sabendo que um campo de futebol tem 4000.0 m2, o estudante fez um programa que recebe
um número em ponto flutuante representando uma área e calcula quantos campos de futebol representam
aquela área.


```
# Cálculo de Campos de Futebol
area = float(input())
campos = area / 4000

print(f"{campos:.1f}")
```


Todavia, o programa ficou muito simples, pois considera apenas uma casa
decimal da divisão. O aluno gostaria que fossem 2 casas decimais. Além,
disso, o aluno quer que o programa funcione para 3 medidas recebidas da entrada padrão, e não
somente uma. Por fim, o aluno gostaria de imprimir a média (em campos de futebol) dos
valores.

## Entrada

No novo programa, 3 áreas serão lidas da entrada padrão (uma em cada linha).

## Saída

Na saída, seu programa deve imprimir em ponto flutuante (2 casas decimais) os valores em campos
de futebol para cada área lida da entrada padrão. Por fim, deve imprimir a média desses
valores.

## Exemplo de Entrada e Saída

```
python solution.py
10000
8000
176000
2.50
2.00
44.00
16.17
```

Note que os três primeiros valores foram lidos da entrada. Depois, há 4 valores impressos. 3 são
resultado do cálculo em campos de futebol, enquanto que o último é a média entre esses 3 valores
calculados.