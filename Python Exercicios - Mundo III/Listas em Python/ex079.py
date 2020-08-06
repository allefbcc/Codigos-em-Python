valores = []

while True :

    n = int(input("Digite um valor: "))

    if n not in valores:

        valores.append(n)
        print("Valor adicionado com sucesso...")

    else:

        print("Valor duplicado! não vou adicionar...")
        
        
    cont = str(input("Quer continuar (S/N)? ")).strip().upper()

    while cont not in "SsNn":
        
         cont = str(input("Resposta Inválida...Quer continuar (S/N)? ")).strip().upper()
        
    
    if cont in "Nn":

        valores.sort()

        break
    
print(f"Você digitou os valores {valores}.")
