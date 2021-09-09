print("Digite 3 números e eu direi qual o maior")

a = int(input("Primeiro número:"))
b = int(input("Segundo número:"))
c = int(input("Terceiro número:"))

if a >= b and a >= c :
    print("O maior número é '%d'" %a)

elif b >= a and b >= c :
    print("O maoir número é '%d'" %b)

elif c >= a and c >= b :
    print("O maior número é '%d'" %c)
