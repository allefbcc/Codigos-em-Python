from datetime import date

genero = str(input("Voce é homem ou mulher? informe com 'M' ou 'F': ")).upper()

if genero == 'M':

    nasc = int(input("informe seu ano de nascimento: "))
    atual = date.today().year

    idade = atual - nasc
    

    if idade < 18:
        print("Vc tem {} anos em {}, ainda vai se alistar".format(idade, atual))

        saldo = 18 - idade

        ano = atual + saldo
    
        print("Falta {} anos para se alistar".format(saldo))
        print("seu alistamento será em: {}.".format(ano))
    

    if idade == 18:
        print("vc tem {} anos em {} é a hora de se alistar".format(idade, atual))

    if idade > 18:
        print("vc tem {} anos em {} e já passou do tempo de se alistar".format(idade, atual))

        saldo = idade - 18
    
        ano = atual - saldo

        print("Passou {} anos do prazo normal".format(saldo))
        print("Seu alistamento foi em: {}".format(ano))

else:
    print("Você é mulher não pode se alistar")
