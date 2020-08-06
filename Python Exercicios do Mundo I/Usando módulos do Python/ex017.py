from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))


#h = pow(pow(co,2) + pow(ca, 2), 0.5)

#print(" O valor da hipotenusa é: {}".format(h))

print("O valor da hipotenusa é: {:.2f}".format(hypot(co, ca)))




