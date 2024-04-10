# IPTU
O valor do IPTU da cidade de Campina Grande é calculado
a partir de dois fatores: a área construída da casa e
uma alíquota que determina o valor por metro quadrado
da região em que a casa se encontra. O valor do IPTU
é o produto da área construída pela alíquota, somado ao
valor fixo de R$ 35,00, referentes à limpeza urbana.

No próximo ano, a Prefeitura Municipal de Campina
Grande
decidiu que o IPTU (Imposto Predial Territorial Urbano)
pode ser pago de formas diferentes, por opção do
contribuinte: em cota única, o que dá direito a um
desconto de 25%; em 6 parcelas, com direito a desconto
de 5%; ou em 10 parcelas, sem direito a desconto.

Pede-se que você escreva um programa que calcule,
para o
contribuinte, o valor do IPTU e as alternativas de
pagamento.

## Entrada

O programa deve ler da entrada apenas dois dados: a
área construída da casa e o valor da alíquota.

## Saída

Na saída deve imprimir o valor do IPTU e as três opções
de pagamento. No caso de parcelamentos, deve indicar o
valor total a ser pago e o valor das parcelas.  Veja no
exemplo dado, como devem ser formatados os dados na
saída. Lembre-se que a formatação deve ser *exatamente*
como indicado nos exemplos.

# Exemplo de Execução

```
$ python3 iptu.py
Área construída? 150.0
Alíquota? 0.89
IPTU: R$ 168.50

Pagamento:
1. Quota única. R$ 126.38
2. Em 6 parcelas. Total: R$ 160.07
   6 x R$ 26.68
3. Em 10 parcelas. Total: R$ 168.50
   10 x R$ 16.85
```