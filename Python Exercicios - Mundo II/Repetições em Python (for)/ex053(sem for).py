frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split() #Coloca as palvras em forma de lista
junto = "".join(palavras) #junta as palavras
inverso = ""

inverso = junto[::-1]

print("O inverso de {} é {}".format(junto, inverso))

if inverso == junto:
    print("Temos um Palindromo")

else:
   print("A frase digitada não é um palindromo!")







