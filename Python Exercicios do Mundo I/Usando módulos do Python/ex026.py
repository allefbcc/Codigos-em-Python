frase = str (input ("Digite uma frase: ")).upper().strip()

print("Ela aparece {} vezes)".format(frase.count("A")))
print("Ela aparece a primeira vez na posição {}".format(frase.find("A")+1))
print("Ela aparece a ultima vez na posição {}".format(frase.rfind("A")+1))
