'''Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

A = [0] * 10
for i in range(10):
    A[i] = int(input("Digite um número: "))

SdQ = 0 #Soma dos Quadrados

for i in range(10):
    SdQ = SdQ + (A[i] ** 2)

print("A soma dos quadrados desses números é: %d" %SdQ)