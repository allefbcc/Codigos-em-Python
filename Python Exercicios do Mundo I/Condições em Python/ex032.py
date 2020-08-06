from datetime import date

print("OBS: se colocar zero, o programa vai considerar o ano atual vc se encontra.")
ano = int(input("informe o ano: "))


if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("é ano Bissexto")
else:
    print("não é")

