termo = int (input("Digite o primeiro termo: "))
razao = int(input("Qual a razão: "))

pa = termo + (10 - 1)* razao


for c in range(termo, pa + razao, razao):
    print(c)


