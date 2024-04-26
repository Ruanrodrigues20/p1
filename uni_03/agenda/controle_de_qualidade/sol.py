p_antes = float(input())
p_depois = float(input())

if p_antes == 0 or p_depois == 0:
    p_antes = float(input())
    p_depois = float(input())
if p_antes == 0 and p_depois == 0:
    p_antes = float(input())
    p_depois = float(input())

porcent_agua = 100 - ((p_depois * 100) / p_antes)

if porcent_agua < 5:
    qualidade = 'Produto qualis A.'
elif porcent_agua >=  5 and porcent_agua < 10:
    qualidade = 'Produto em conformidade.'
else:
    qualidade = 'Produto não conforme.'

print(f'{porcent_agua:.1f}% do peso do produto é de água congelada.')
print(qualidade)