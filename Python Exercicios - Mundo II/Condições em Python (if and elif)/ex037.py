num = int(input("Digite um numero: "))

print(" 1 - para binário")
print(" 2 - para octal")
print(" 3 - para hexadecimal")

conversao = int(input("Escolha a base de conversão de 1 a 3: "))

if conversao == 1:
   print(bin(num)[2:])

elif conversao == 2:
    print(oct(num)[2:])

elif conversao == 3:
    print(hex(num)[2:])
    
else:
     print("Escolha Invalida")
    



