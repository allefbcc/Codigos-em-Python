preco = float(input("Informe o preço: "))

print("Escolha a opção de pagamento: ")
print(" 1 - Á vista: dinheiro / cheque")
print(" 2 - Á vista no cartão")
print(" 3 - Até 2x no cartão")
print(" 4 - 3x ou mais no cartão")

opcao = int(input("Sua opção: "))

if opcao == 1:

    desc = (preco * 10) / 100
    atual = preco - desc

    print("Á vista no cheque / dinheiro, tem 10% de desconto, o valor passar a ser {:.2f} R$.".format(atual))

            
elif opcao == 2:
    
    desc = (preco * 5) / 100
    atual = preco - desc

    print("Á vista no cartão, tem 5% de desconto, o valor passar a ser {:.2f} R$.".format(atual))

elif opcao == 3:

    parc = preco / 2
    
    print("Sua compra será parcelada em 2x de {:.2f}.".format(parc))
    print("Áté 2x no cartão, o valor passar a ser o preco normal sem juros: {:.2f} R$.".format(preco))

elif opcao == 4:

    juros = (preco * 20) / 100 
    atual = preco + juros

    totalparc = int(input("Quantas parcelas: "))
    parc = atual / totalparc

    print("Sua compra será parcelada em {}x de {:.2f} com Juros.".format(totalparc, parc))
    print("Áté 3x ou mais corre juros de 20%: {:.2f} R$.".format(atual))

else:
    print("Opção Invalida")
