# Expressão Regular Simples

Uma forma de descrever um gerador de palavras através de um modelo é utilizar o
caractere '\*'. Por exemplo, a string 'oba\*prog1' define um conjunto de palavras
que obedecem a regra: deve começar com 'oba', pode conter qualquer sequencia não vazia de
caracteres depois do 'oba' e deve terminar com 'prog1'. Nesse caso a sequência
'obadisciplinaprog1' satisfaz a expressão 'oba\*prog1', enquanto 'naoobaminiprog1'
não satisfaz.

Escreva uma função **is\_substring\_expr(str1,str2)** que verifica se str1 satisfaz
a expressão regular str2. str2 sempre assume a forma uma_string\*outra_string.
Em caso afirmativo, a função deve retornar True. Caso contrário, deve retornar False.

## Atenção

Assuma que só existe um '\*'.
Assuma que os termos separados por '\*' são diferentes.

Você pode usar if, mas não é permitido utilizar o comando if em conjunto com o in.
Também não é permitido usar endswith e startswith.

## Exemplos e Asserts

    assert is_substring_expr('oicarovoce','oi*voce')
    assert is_substring_expr('oicvoce','oi*voce')