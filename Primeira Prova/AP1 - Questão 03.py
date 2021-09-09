#Luiz Eduardo Alves Camurça - 508200


n = int(input("Numero de termos: "))

#Excluindo números menores que 2
while n < 2:
    print("valor invalido")
    n = int(input("Numero de termos: "))

#Declarando Variáveis
y = 0
x = 0       # Sendo y o antecessor de x
soma = 0

#Repetindo a formula para todos os números da sequência
for i in range(1,n+1):

    #Guardando o valor do número anterior
    y = x

    #Pedindo os números da sequência
    x = int(input("numero: "))

    #Guardando o valor da maior soma de números consecutivos
    if x - y > 0 and x + y > soma:
        soma = x + y
        termo1 = x 
        termo2 = y 

print("max. %d e seq. %d, %d" % (soma, termo2, termo1))
