import math

ang = float(input("Digite o valor do angulo: "))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print("O seno é {:.2f}\nO cosseno é {:.2f}\nA tangente é {:.2f}".format(seno, cosseno, tangente))

