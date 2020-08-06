from datetime import date

nasc = int(input("Informe seu ano de nascimento: "))

atual = date.today().year

idade = atual - nasc

if idade <= 9:
    print("Você tem {} anos.".format(idade))
    print("Você está na categoria: MIRIM")

elif idade <= 14:
    print("Você tem {} anos.".format(idade))
    print("Você está na categoria: INFANTIL")

elif idade <= 19:
    print("Você tem {} anos.".format(idade))
    print("Você está na categoria: JUNIOR")

elif idade <= 25:
    print("Você tem {} anos.".format(idade))
    print("Você está na categoria: SÊNIOR")

elif idade > 25:
    print("Você tem {} anos.".format(idade))
    print("Você está na categoria: MASTER")
    
