a_construida = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

iptu = a_construida * aliquota + 35

print(f'IPTU: R$ {iptu:.2f}')

cota_unica = iptu - ((iptu * 25)/100)
cota_6p = iptu - ((iptu * 5)/100)
parcelas_6 = cota_6p / 6
cota_10p = iptu
parcelas_10 = cota_10p / 10

print(f"""
Pagamento:
1. Quota única. R$ {cota_unica:.2f}
2. Em 6 parcelas. Total: R$ {cota_6p:.2f}
   6 x R$ {parcelas_6:.2f}
3. Em 10 parcelas. Total: R$ {cota_10p:.2f}
   10 x R$ {parcelas_10:.2f}""")
