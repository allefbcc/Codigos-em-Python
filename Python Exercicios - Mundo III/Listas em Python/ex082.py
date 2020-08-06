lista = []
listapar = []
listaimp = []

while True:

    n = int(input("Digite um número: "))
    lista.append(n)
    resp = str(input("Quer continuar (S/N)? ")).strip().upper()

    if n % 2 == 0:
        listapar.append(n)

    else:
        listaimp.append(n)

    while resp not in "SsNn":

        resp = str(input("Quer continuar (S/N)? ")).strip().upper()


    if resp in "Nn":

        break

print("="*30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {listapar}")
print(f"A lista de ímpares é {listaimp}")
