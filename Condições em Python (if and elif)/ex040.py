n1 = float(input("Digite a 1° nota: "))
n2 = float(input("Digite a 2° nota: "))

m = (n1 + n2) / 2

if m < 5:
    print("Sua média é {:.1f} e vc está: REPROVADO".format(m))

elif m >= 5 and m < 7:
    print("sua média é {:.1f} e vc está de: RECUPERAÇÃO".format(m))

elif m >= 7:
    print("Sua média é {:.1f} e vc está: APROVADO".format(m))
