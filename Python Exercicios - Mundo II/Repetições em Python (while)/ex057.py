
sexo = str(input("Informe seu sexo (F/M): ")).strip().upper()


while sexo != "F" and sexo != "M":
    sexo = str(input("Informação inválida, digite novamente seu sexo (F/M): ")).strip().upper()

print("Sexo {} registrado no sistema".format(sexo))
    

    

