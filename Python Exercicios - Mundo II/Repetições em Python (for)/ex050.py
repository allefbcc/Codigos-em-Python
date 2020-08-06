soma = 0
cont = 0

for c in range(1, 7):
    nump = int(input("Digite um numero: ".format(c)))

    if nump % 2 == 0:
        soma = soma + nump
        cont = cont + 1

print("Você informou {} numeros Pares e a soma foi: {}".format(cont, soma))
