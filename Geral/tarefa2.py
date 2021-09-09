capacidade = int(input("Capacidade: "))

while capacidade <= 0:
    print("Valor Inválido!")
    capacidade = int(input("Capacidade: "))


fluxo = int(input("Fluxo: "))
população = 0 + fluxo

while população < 0:
    print("valor inválido")
    fluxo = int(input("Fluxo: "))
    população = fluxo

if população >= capacidade * 2:
    print("vamos partir")

else:
    while população <= (capacidade * 2):
        população = população + fluxo

        if população < 0:
            print("valor inválido")
            população = população - fluxo
            fluxo = int(input("Fluxo: "))
            população = população + fluxo
            
        
        if população == 0:
            print("vazio")
            fluxo = int(input("Fluxo: "))
            população = população + fluxo

        if população > 0 and população < capacidade:
            print("ainda há espaço")
            fluxo = int(input("Fluxo: "))
            população = população + fluxo

        if população == capacidade:
            print("lotado")
            fluxo = int(input("Fluxo: "))
            população = população + fluxo

        if população >= capacidade * 2:
            print("vamos partir")
            população = população + fluxo