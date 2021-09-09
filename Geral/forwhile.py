"""num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

while num1<0 and num2<0:
    print("Digite numeros positivos!")
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))

print(num1)
print(num2)

while True:
    idade = int(input("DIGITE SUA IDADE: "))
    if idade>0:
        break
print ("%d é a sua idade"%(idade))"""

#Cálculo de IMC
#O Comando "While" é útil para impossibilitar respostas inválidas e para repertir um programa

#utilizei a variável "repetição" para sempre recomeçar o código
repetição = 1
while repetição == 1:
    #adquirindo as informações necessárias para calcular o IMC
    print("Calculo de IMC:")
    altura = float(input("Digite sua altura em metros: "))
    peso = float(input("Digite seu peso em quilogramas: "))
    #impossibilitando o uso de valores absurdos, como 0 e negativos
    while altura<0 or peso<0:
        print("Digite um número maior que 0")
    #calculando o IMC
    imc = (peso/(altura * altura))
    #exibindo o resultado
    print("Seu IMC é, aproximadamente, %d" %imc)
