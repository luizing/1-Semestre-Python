#Programa que diz quanto tempo um motorista gastará para chegar a seu destino (partindo de um ponto específico)

print("Fortaleza = 1")
print("Natal = 2")
print("Sobral = 3")

destino = int(input("Para onde você está indo? "))

if destino == 1:
    print("Fortaleza: O tempo estimado é de 35 min (50 km)")

elif destino == 2:
    print("Natal: O tempo estimado é de 6 h 46 min (494 km)")

elif destino == 3:
    print("Sobral: O tempo estimado é de 4 h 15 min (315 km)")

else:
    print("Digite um número valido!")