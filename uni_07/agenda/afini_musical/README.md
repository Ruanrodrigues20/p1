# Afinidade Musical

Uma métrica utilizada pelo facebook para sugerir
amigos a um determinado usuário é utilizar o conceito
de afinidade musical. A ideia é simples. A partir de
duas listas de artistas que dois usuários gostam,
o sistema considera que há afinidade musical
se os dois gostam de 3 ou mais artistas iguais.

Implemente a função tem\_afinidade(l1, l2) que retorna
verdadeiro caso os usuários possuam afinidade e
falso, caso contrário.

## Exemplos de asserts

    l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
    l2 = ['zeze', 'joao', 'u2', 'jquest']
    assert tem_afinidade(l1, l2) == True