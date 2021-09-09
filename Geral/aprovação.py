nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print("Parabéns! Você foi aprovado")
    print("Sua média foi %d !" %media)

elif media >= 4 and media < 7:
    print("Você precisará fazer uma Avaliação Final.")
    print("Sua média foi %d ." %media)

else:
    print("F. Tá reporvado marreco.")
    print("Tirou %d na média? Aí é foda." %media)