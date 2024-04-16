n = int(input())

cont = 0
for i in range(n):
    palavra = input()
    if len(palavra) >= 3 and palavra[0] == palavra[-1]:
        cont += 1

print(cont)