n = int(input())
repeticoes = int(input())

cont = 0
for i in range(repeticoes):
    num = int(input())
    if num % n == 0:
        cont += 1

porcentagem = (cont * 100) / repeticoes
print(f'{cont} ({porcentagem:.1f}%)')