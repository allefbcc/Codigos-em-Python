opc = 0


print("="* 15)
print(" Menu de opções ")
print("="* 15)

num = int(input(" Digite o 1° numero: "))
num2 = int(input(" Digite o 2° numero: "))

while opc != 5:
    
    print(" Escolha uma opção:\n ")

    print(" 1 - Somar")
    print(" 2 - multiplicar")
    print(" 3 - maior")
    print(" 4 - novos numeros")
    print(" 5 - sair do programa\n")

    opc = int(input(" Sua opção: "))

    if opc == 1:

        soma = num + num2
        
        print(" Você escolheu a opção de SOMAR!")
        print(" O resultado da soma de {} e {} é: {}\n".format(num, num2, soma))

    elif opc == 2:

        multi = num * num2

        print(" Você escolheu a opção de MULTIPLICAR!")
        print(" O resultado da multiplicação de {} e {} é: {}\n".format(num, num2, multi))

    elif opc == 3:

       if num > num2:
           print(" Você escolheu a opção MAIOR dos números!")
           print(" O número maior entre {} e {} é: {}\n".format(num, num2, num))

       else:
            print(" Você escolheu a opção MAIOR dos números!")
            print(" O número maior entre {} e {} é: {}\n".format(num, num2, num2))

    elif opc == 4:
        
        num = int(input(" Digite um novo numero: "))
        num2 = int(input(" Digite outro numero: "))

    elif opc > 5:
        print("Opção inválida, tente novamente")



if opc == 5:
    print(" Você saiu do programa!")



        
        
