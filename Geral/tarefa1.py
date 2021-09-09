#tarefa 1
#Luiz Eduardo Alves Camurça - 508200

#Adquirindo os números A e B.
print("O número 'B' deve ser maior que o número 'A'")
A = int(input("Digite o número A: "))
B = int(input("Digite o número B: "))

#Invalidando valores de A e B.
while B<=A:
    print("invalido")
    A = int(input("Digite o número A: "))
    B = int(input("Digite o número B: "))

#Enquanto não há valor para i, a soma não existe, logo está como 0.
soma = 0

#Separando os números que têm as condições necessárias para entrar na soma (ser impar e divisível por 2)
for i in range(A,B+1):
    if i % 2 != 0 and i % 3 == 0:
        
            #Somando esses valores
            soma = soma + i 

#Mostrando o resultado da soma
print(soma)
