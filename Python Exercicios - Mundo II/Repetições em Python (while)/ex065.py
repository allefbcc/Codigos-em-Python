resp = "S"

soma = 0
cont = 0

media = 0

maior = 0

menor = 0

while resp == "S":

    n = int(input("Digite um numero: "))
    
    soma += n
    cont += 1

    if cont == 1:
        
        maior = n
        menor = n
        
    else:
        
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    resp = str(input("Quer continuar? (S/N): ")).upper().strip()[0]

media = soma / cont

print("Você digitou {} números e a média foi: {} ".format(cont, media))
print("O maior valor foi {} e o menor foi {} ".format(maior, menor))
