soma = 0
produto = 0

cont = 0
menor = 0

barato = 0

print("="*30)
print("MUNDÃO DO BARATO")
print("="*30)

while True:
    
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço: "))
    continuar = " "

    while continuar not in "SsNn":

        continuar = str(input("Quer continuar (S/N)? ")).strip().upper()[0]

    soma += preco
    cont += 1
    

    if preco > 1000:

        produto += 1

    if cont == 1 or preco < menor:

        menor = preco
        barato = nome

    if continuar == "N":

        break
    
print(f"Sua compra total deu o valor de: {soma} R$")
print(f"teve {produto} produtos com valor superior a 1000 R$")
print(f"O produto mais barato foi {barato} e custou {menor} R$")
    

        
