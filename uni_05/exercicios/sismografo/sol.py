i = 0
media = 0
nums = 0
while True:
    medicoes = float(input())
    i += 1
    nums += medicoes
    media = nums / i
    print(f'm = {medicoes:.1f} (média = {media:.1f})')
    if medicoes > 10:
        break

print('ALERTA: limite de sismo atingido!')
print(f'número de medições: {i}')