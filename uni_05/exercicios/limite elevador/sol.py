razao_max = float(input())

cont_a = 0
cont_c = 0
cont_pessoa = 0
peso_t = 0
peso_f = 0
while True:
    dados = input().split()
    peso = float(dados[1])
    peso_t += peso

    if cont_pessoa == 0 and dados[0] == 'c': break

    if dados[0] == 'c':
        cont_c += 1
    elif dados[0] == 'a':
        cont_a += 1

    razao = cont_c / cont_a

    if razao <= razao_max and peso_t < 700:
        cont_pessoa += 1
        peso_f += peso
    else: break

print('Limite atingido.')
print(f'Elevador saiu com {cont_pessoa} pessoas e {peso_f:.2f} kg.')