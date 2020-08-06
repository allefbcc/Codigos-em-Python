salario = float (input("Informe seu salario: "))

aumento = (salario * 10) / 100 + salario

aumento2 = (salario * 15) / 100 + salario

if salario > 1250:
    print("O seu salario teve um aumento de 10% e passa a ser: {} R$".format(aumento))

if salario <= 1250:
    print("O seu salario teve um aumento de 15% e passa a ser: {} R$".format(aumento2))
