
print("="*50)
print("{:^50}".format("BANCO ALLEN"))
print("="*50)

valor = int(input("Qual valor você quer sacar? "))

total = valor  
ced = 50
totalced = 0

while True:
    
    if total >= ced:

        total -= ced

        totalced += 1

    else:

        if totalced > 0:
            
            print(f"Total de {totalced} cédulas de {ced} R$")

        if ced == 50:
            ced = 20
            
        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        totalced = 0
        
        if total == 0:
            break
