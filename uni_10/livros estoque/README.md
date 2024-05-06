# Estoque de Livros

Escreva uma função **ausentes(estoque)** que receba um dicionário contendo informações sobre o
estoque de uma livraria (titulo:quantidade). Sua função deve retornar a
quantidade de títulos que estão zerados no estoque.

## Exemplo de assert

    livros = { "Metamorfose": 30, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
    assert ausentes(livros) == 2