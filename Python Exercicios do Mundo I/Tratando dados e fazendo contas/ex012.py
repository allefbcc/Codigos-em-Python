preco = float(input("Digite o preço do produto: "))

desconto = preco * 5 / 100

novopreco = preco - desconto

print("Este produto está com desconto de 5% e seu valor atual é: {:.2f}".format(novopreco))

