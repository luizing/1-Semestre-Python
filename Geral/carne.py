
#Cabeçalho
print("Digite 'sim' para afirmativo ou qualquer outra coisa para negativo")
estrelas = 0


a = str(input("A carne está com gordura branca e firme? "))
if a == "sim":
    estrelas = estrelas + 1
else:
    estrelas = estrelas

b = str(input("A carne possui cor vermelho-brilhante? "))
if b == "sim":
    estrelas = estrelas + 1
else:
    estrelas = estrelas    

c = str(input("A carne está em uma temperatura inferior a 7 graus? "))
if c == "sim":
   estrelas = estrelas + 1

else:
    estrelas = estrelas

d = str(input("A carne possui cheiro agradável? "))
if d == "sim":
    estrelas = estrelas + 1

else:
    estrelas = estrelas

e = str(input("A carne ainda está dentro do prazo de validade? "))
if e == "sim":
    estrelas = estrelas + 1

else:
    estrelas = 0

if estrelas >= 3:
    print("A carne passou no teste!")

else:
    print("A carne não passou no teste!")


print(estrelas,"Estrelas")