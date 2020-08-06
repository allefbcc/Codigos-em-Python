casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Quantos anos vai pagar? "))

prest = casa / (anos * 12)
minimo = salario * 30 / 100

print("\nPara pagar uma casa de {:.2f} R$ em {} anos".format(casa, anos), end = " ")
print("a prestação será de {:.2f} R$".format(prest))

if prest <= minimo:
    
    print("Emprestimo pode ser feito")
else:
    print("emprestimo negado")
