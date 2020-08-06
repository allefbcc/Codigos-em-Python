lista = []

cont = 0

cont5 = 0

while True:

    n = int(input("Digite um número: "))
    lista.append(n)
    resp = str(input("Quer continuar (S/N): ")).strip().upper()

    cont += 1

    while resp not in "SsNn":

        resp = str(input("Quer continuar (S/N): ")).strip().upper()


    if resp in "Nn":
        
        break


lista.sort(reverse = True)

print("="*30)
print(f"Foram digitados um total de {cont} números!")
print(f"A lista de números é {lista}")
        
if 5 in lista:

    print("O número 5 está presente na lista")

else:

    print("O número 5 NÃO está na lista")
