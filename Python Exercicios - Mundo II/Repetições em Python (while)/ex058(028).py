import random
from time import sleep

num = int(input("Digite um numero entre 0 e 10: "))

num1 = random.randint(1,10)

tentativas = 1

if num < num1:
    print("É MAIS")

elif num > num1:
    print("É MENOS")


while num != num1:
    
    num = int(input("Você errou, tente novamente: "))

    tentativas += 1

    if num < num1:
        print("É MAIS")

    elif num > num1:
        print("É MENOS")


print("Você acertou, o numero era {} e você precisou de {} tentativas.".format(num, tentativas))
