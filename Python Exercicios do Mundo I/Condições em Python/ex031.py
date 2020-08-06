dist = float(input("Informe a distancia: "))

preco1 = dist * 0.5

preco2 = dist * 0.45

if dist <= 200:
    print("O valor a ser pago é: {} R$".format(preco1))
else:
    print("O valor a ser pago é: {} R$".format(preco2))
