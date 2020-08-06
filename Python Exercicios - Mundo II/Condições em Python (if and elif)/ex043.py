peso = float(input("Informe o peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu IMC é {:.2f} e você está: Abaixo do peso".format(imc))

elif imc >= 18.5 and imc < 25:
    print("Seu IMC é {:.2f} e você está com: Peso ideal".format(imc))

elif imc >= 25 and imc < 30:
    print("Seu IMC é {:.2f} e você está: Sobrepeso".format(imc))

elif imc >= 30 and imc < 40:
    print("Seu IMC é {:.2f} e você está com: Obesidade".format(imc))

elif imc >= 40:
    print("Se IMC é {:.2f} e você está com: Obsedidade mórbida".format(imc))

