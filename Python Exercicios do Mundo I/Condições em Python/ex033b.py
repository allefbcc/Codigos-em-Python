a = int (input("Informe o primeiro numero: "))
b = int (input("Informe o segundo numero: "))
c = int (input("Informe o terceiro numero: "))

menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c


maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print("o menor valor digitado foi: {} ".format(menor))
print("o maior valor digitado foi: {} ".format(maior))

