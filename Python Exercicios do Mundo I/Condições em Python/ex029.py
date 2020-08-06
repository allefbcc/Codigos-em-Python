v = int(input("Informe a velocidade: "))

m = (v-80)*7

if v > 80:
    print("Vc foi multado, o valor da multa é: {} R$".format(m))
else:
    print("pode ir tranquilo")
