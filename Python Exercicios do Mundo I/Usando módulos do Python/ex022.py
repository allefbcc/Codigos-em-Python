nome = str (input("Digite seu nome completo: ")).strip()

print(nome.upper())
print(nome.lower())

print("Seu nome ao todo tem {} letras.".format(len(nome) - nome.count(" ")))


nome1 = nome.split()
print("Seu primeiro nome tem {} letras.".format(len(nome1[0])))

