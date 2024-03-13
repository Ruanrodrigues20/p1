nota_a1 = float(input())
nota_a2 = float(input())
nota_a3 = float(input())
idade_a = int(input())
nota_b1 = float(input())
nota_b2 = float(input())
nota_b3 = float(input())
idade_b = int(input())

media_a = (nota_a1 * 3 + nota_a2 * 4 + nota_a3 * 3) / 10
media_b = (nota_b1 * 3 + nota_b2 * 4 + nota_b3 * 3) / 10

if media_a > media_b:
    print(f'O primeiro candidato foi aprovado com nota {media_a:.1f}')
elif media_b > media_a:
    print(f'O segundo candidato foi aprovado com nota {media_b:.1f}')
else:
    if idade_a > idade_b:
       print(f'O primeiro candidato foi aprovado com nota {media_a:.1f}')
    elif idade_b > idade_a:
        print(f'O segundo candidato foi aprovado com nota {media_b:.1f}')
    else:
        print('Empate')
