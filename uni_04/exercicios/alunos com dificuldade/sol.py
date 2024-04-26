alunos = input().split()
nums = [float(n) for n in input().split()]

notas = []
media_turma = 0.0
for i in range(0 ,len(nums) - 1, 2):
    media_i = (nums[i] + nums[i + 1]) / 2
    media_turma += media_i
    notas.append(media_i)

media_turma = media_turma / len(alunos)

for j in range(1, len(alunos)):
    if notas[j] < media_turma:
        print(f'- {nums[2 * j]:.1f} {nums[2 * j + 1]:.1f} ({notas[j]:.1f}) {alunos[j]}')

print(f'> media turma: {media_turma:.2f}')