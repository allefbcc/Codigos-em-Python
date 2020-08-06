num = int (input("Digite um numero: "))

cont = 0

for c in range(1, num + 1):

    if num % c == 0:
        cont = cont + 1

    print(c)
    
print("o numero {} foi divisivel {} vezes".format(num, cont))


if cont == 2:
    print("É Primo")

else:
    print("Não é primo")

