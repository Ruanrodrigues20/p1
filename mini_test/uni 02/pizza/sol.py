n_pessoas = int(input())
n_pizza = int(input())
p_pizza = float(input())

q_fatias = (n_pizza *  8) // n_pessoas
fatias_sobra = (n_pizza * 8) % n_pessoas
total = n_pizza * p_pizza

print(f'{q_fatias} fatia(s) para cada um e sobra(m) {fatias_sobra} fatia(s)')
print(f'Valor total: R$ {total:.2f}')