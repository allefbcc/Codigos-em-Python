from datetime import date

nasc = int(input("informe seu ano de nascimento: "))
atual = date.today().year

idade = atual - nasc

if idade < 18:
    print("Vc tem {} anos em {}, ainda vai se alistar".format(idade, atual))

    saldo = 18 - idade

    ano = atual + saldo
    
    print("Falta {} anos para se alistar".format(saldo))
    print("seu alistamento será em: {}.".format(ano))
    

elif idade == 18:
    print("vc tem {} anos em {} é a hora de se alistar".format(idade, atual))

elif idade > 18:
    print("vc tem {} anos em {} e já passou do tempo de se alistar".format(idade, atual))

    saldo = idade - 18
    
    ano = atual - saldo

    print("Passou {} anos do prazo normal".format(saldo))
    print("Seu alistamento foi em: {}".format(ano))


