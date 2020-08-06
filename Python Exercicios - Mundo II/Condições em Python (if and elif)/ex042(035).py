r1 = float(input("informe o comprimento a: "))
r2 = float(input("informe o comprimento b: "))
r3 = float(input("informe o comprimento c: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    
    print("os comprimentos acima podem formar um triangulo")

    if r1 == r2 == r3:
        print("Todos os lados são iguais: Triangulo EQUILÁTERO")

    elif r1 != r2 != r3 != r1:
        print("Todos os lados são diferentes: Triangulo ESCALENO")

    else:
        print("Dois lados são iguais: Triangulo ISÓSCELES")
        
else:
    print("os comprimentos acima NÃO podem formar um triangulo")




