num = int(input(" Informe um número para calcular seu fatorial: "))

f = 1

for c in range(num, 0, -1):

    f *= c
    
    print(f)
    
