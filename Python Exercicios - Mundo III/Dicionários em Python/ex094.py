
galera = list()
pessoa = dict()
soma = média = 0

while True:

    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))

    while True:
        pessoa["Sexo"] = str(input("Sexo (M/F): ")).upper()[0]

        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")

    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())
    
    while True:
        resp = str(input("Quer continuar (S/N)? ")).upper()[0]

        if resp in "SN":
            break

        print("ERRO! Responda apenas S ou N.")

    if resp == "N":
            break
        
print("="*30)
print(f" A) Ao todo temos {len(galera)} pessoas cadastradas.")
média = soma / len(galera)
print(f" B) A média de idade é {média:5.2f} anos.")
print(f" C) As mulheres cadastradas foram ", end = " ")

for p in galera:
    if p["Sexo"] in "F":
        print(f"{p['Nome']}", end = " ")
print()

print(" D) Lista das pessoas que estão acima da média: ")

for p in galera:
    if p["Idade"] >= média:
        print("   ")

        for k, v in p.items():
            print(f"{k} = {v};", end = " ")
        print()
        
print("<<ENCERRADO>>")
