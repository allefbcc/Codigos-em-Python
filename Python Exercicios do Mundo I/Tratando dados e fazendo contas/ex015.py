kmperc = float(input("Qual a quantidade de km percorridos? "))

qtd = int(input("Qual a quantidade de dias que ele foi alugado? "))

preco = (60 * qtd) + (0.15 * kmperc)

print(" O preço a pagar é de: {:.2f} ".format(preco))
