#Luiz Eduardo Alves Camurça - 508200

verificado = int(input("numero a ser verificado: "))
ocorrencias = 0 #número de vezes em que o "verificado" apareceu

#Excluindo valores inválidos.
while verificado < 0 or verificado > 9:
    verificado = int(input("numero a ser verificado: "))

telefone = int(input("numero de telefone: "))

#Variáveis auxiliáres para verificar o número de dígitos de "telefone".
telefoneTeste = telefone
testeDigitos = telefone + 1

#Excluindo valores de "telefone" com menos de 8 digitos e mais de 9 digitos.
while telefoneTeste < testeDigitos:

    #Caso o número de telefone digitado tenha menos de 8 dígitos ou inicie com um 0, ao ser dividido por 10**7, ele será menor que 0.
    #Caso tenha mais de 9 digitos, depois da mesma divisão, ele será maior que 100.
    telefoneTeste = telefoneTeste / (10**7)
    if telefoneTeste >= 1 and telefoneTeste < 10:
        digitos = 8
        telefoneTeste = testeDigitos + 1

    #Separei os casos com um elif para guardar o número de dígitos do telefone e usar isso no futuro.
    elif telefoneTeste < 100:
        digitos = 9
        telefoneTeste = testeDigitos+1

    else:
        telefone = int(input("numero de telefone"))
        telefoneTeste = telefone
        testeDigitos = telefone + 1

#Início do programa propriamente dito.

#variaveis auxiliares
telefoneA = telefone
anterior = 0
digitosMaiores = 0

if digitos == 8:
    digitosRestantes = 8 #variavel responsável por repetir a estrutura para todos os números

    while digitosRestantes > 0:
        anterior = digitosMaiores #variavel responsável por guardar os primeiros digitos do telefone

        digitosMaiores = telefoneA // (10**(digitosRestantes-1)) #formula para separar os primeiros digitos do restante

        telefone = digitosMaiores - (anterior * 10) #formula para separar os digitos em sua ordem
        
        if telefone == verificado:  #caso o número seja igual ao que foi informado, isso contará como uma ocorrencia
            ocorrencias = ocorrencias + 1
            

        digitosRestantes = digitosRestantes - 1
        
#a estrutura para números de 9 digitos é a mesma

if digitos == 9:
    digitosRestantes = 9 #variavel responsável por repetir a estrutura para todos os números

    while digitosRestantes > 0:
        anterior = digitosMaiores #variavel responsável por guardar os primeiros digitos do telefone

        digitosMaiores = telefoneA // (10**(digitosRestantes-1)) #formula para separar os primeiros digitos do restante


        telefone = digitosMaiores - (anterior * 10)  #formula para separar os digitos em sua ordem
        
        if telefone == verificado: #caso o número seja igual ao que foi informado, isso contará como uma ocorrencia
            ocorrencias = ocorrencias + 1
            
    
        digitosRestantes = digitosRestantes - 1
    
print(ocorrencias)