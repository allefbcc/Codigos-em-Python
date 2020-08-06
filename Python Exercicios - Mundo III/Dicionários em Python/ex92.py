from datetime import datetime


pessoa = dict()

atual = datetime.now().year

pessoa["Nome"] = str(input("Nome: "))

nasc = int(input("Ano de Nascimento: "))

pessoa["Idade"] = atual - nasc


pessoa["Ctps"] = int(input("Carteira de Trabalho (0 não tem): "))


if pessoa["Ctps"] != 0:

    pessoa["Contratação"] = int(input("Ano de Contratação: "))

    pessoa["Salário"] = float(input("Salário: R$ "))

    pessoa["Aposentadoria"] = pessoa["Idade"] + ((pessoa["Contratação"] + 35) - atual)
    

print("="*30)
for k,v in pessoa.items(): 
    print(f" {k} tem o valor: {v}")
    



