#Luiz Eduardo Alves Camurça - 508200

pontosDoTrajeto = int(input("Pontos do Trajeto: "))

#Exclusão de valores inválidos para os pontos do trajeto
while pontosDoTrajeto < 2 or pontosDoTrajeto > 1000:
    print("entrada invalida")
    pontosDoTrajeto = int(input("Pontos do Trajeto: "))

#Variaveis
altura = 0
esforço = 0
esforço1 = 0
altura1 = 0

#Estrutura de Repetição
while pontosDoTrajeto > 0:

    #Forma de guardar a altura anterior
    altura1 = altura

    #Pegando a primeira altura e as alturas seguintes
    altura = int(input("altura: "))

#Exclusão de alturas inválidas
    while altura <= 0:
        print("entrada invalida")
        altura = int(input("altura: "))

    #Caso o trajeto seja uma descida (da esquerda para a direita)
    if altura - altura1 <= 0:
        esforço = esforço
        esforço1 = esforço1 + (altura1 - altura)

    #Utilizado para a primeira altura digitada no programa não ser somada ao esforço no resultado final
    elif altura1 == 0:
        auxiliar = 0

    #Caso o trajeto seja uma subida (da esquerda para a direita)
    else:
        esforço = esforço + (altura - altura1)
        esforço1 = esforço1

    pontosDoTrajeto = pontosDoTrajeto - 1

#Mostrando o resultado final
if esforço >= esforço1:
    print(esforço1)
else:
    print(esforço)
