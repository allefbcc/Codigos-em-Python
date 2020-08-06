import random
from time import sleep

print("Suas Opções:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

opc = int(input("Escolha Sua Jogada: "))

nomes = ['Pedra', 'Papel', 'Tesoura']

pc = random.choice(nomes)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")

if opc == 1 and pc == "Pedra":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Deu Empate")
    

elif opc == 1 and pc == "Papel":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("O COMPUTADOR venceu")


elif opc == 1 and pc == "Tesoura":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Você Venceu")


##############################################

elif opc == 2 and pc == "Pedra":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Você Venceu")

elif opc == 2 and pc == "Papel":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Deu Empate")

elif opc == 2 and pc == "Tesoura":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("O COMPUTADOR Venceu")

##############################################

elif opc == 3 and pc == "Pedra":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("O COMPUTADOR Venceu")

elif opc == 3 and pc == "Papel":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Você Venceu")

elif opc == 3 and pc == "Tesoura":

    print("O Jogador escolheu: {}.".format(nomes[opc - 1]))
    print("O PC escolheu: {}.".format(pc))
    print("Deu empate")

elif opc == 0 or opc >= 4:
    print("JOGADA INVÁLIDA, TENTE NOVAMENTE")

