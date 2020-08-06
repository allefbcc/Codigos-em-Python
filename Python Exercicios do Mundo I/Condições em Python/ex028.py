import random
from time import sleep

numero = int (input("Adivinhe o numero: "))

numero1 = random.randint(0, 5)

print("PROCESSANDO...")
sleep(2)

if numero == numero1:
    print("Vc acertou")
else:
    print("Vc errou")
