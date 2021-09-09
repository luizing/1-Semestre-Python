nota = [0] * 5
for i in range(0,5):
    nota[i] = float(input("Nota do aluno %d: " %(i+1)))


media = 0
for i in range(0,5):
    media = media + nota[i]
media = media / len(nota)

print("A média da turma é %d" %media)

for i in range(5):
    if nota[i] >= 4 and nota[i] < 7:
        print("O aluno %d ficou de AF e sua nota foi %d" %(i+1,nota[i]))