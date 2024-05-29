# Roteiros Aeroportos

Os aeroportos são identificados através de um código
definido pela IATA (Associação Internacional de
Transporte Aéreo). O código IATA é formado por 3 letras
e designa unicamente um aeroporto. Por exemplo, o código
IATA para o Aeroporto João Suassuna em Campina Grande é
CPV, o Aeroporto Tom Jobim no Rio de Janeiro é GIG e o
Aeroporto de Guarulhos em São Paulo é GRU.

Uma outra informação importante vinculada a cada
aeroporto é a indicação dos vôos diretos que tem origem
no referido aeroporto. Por exemplo, os aeroportos que
são contemplados com vôos diretos que partem de CPV
(aeroporto de Campina Grande) são REC e SSA. Isso indica
que é possível sair de CPV e chegar em REC, sem escalas.
Da mesma forma, é possível sair  de CPV e chegar em SSA,
sem escalas.

Um roteiro de viagem aérea pode ser visto como uma
composição de vôos diretos entre aeroportos. O roteiro
Campina Grande/Recife/São Paulo/Brasília/Campina Grande
indica que o vôo sai de campina Grande para Recife,
depois de Recife para São Paulo, depois de São Paulo
para Brasília e, finalmente, de Brasília para Campina
Grande.

Crie uma função que recebe dois mapas (um com o
mapeamento do código IATA para os aeroportos e outro com
as informações de vôos diretos de cada aeroporto) e um
roteiro de viagem aérea. A função deve retornar True se
o roteiro é possível de ser realizado e False, caso
contrário. Vamos assumir que cada cidade tem apenas um
aeroporto e que o roteiro de viagem contempla pelo menos
duas cidades.

# Exemplos de asserts

```
iata = {"Campina Grande": "CPV",
           "Recife": "REC",
           "Salvador": "SSA",
           "Brasilia": "BSB",
           "Sao Paulo": "GRU",
           "Rio de Janeiro": "GIG"}


voos = {"CPV": ["REC", "SSA"],
           "REC": ["CPV", "BSB", "GRU", "GIG"],
           "SSA": ["REC", "GRU", "GIG"],
           "BSB": ["CPV", "GIG", "GRU"],
           "GRU": ["GIG", "BSB"],
           "GIG": ["GRU", "REC"]}

assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")

```