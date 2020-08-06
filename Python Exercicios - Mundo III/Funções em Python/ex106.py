from time import sleep

def ajuda(com):
    título(f"\nAcessando o manual do comando {com}")
    help(com)
    sleep(2)

def título(msg):
    tam = len(msg) + 4
    print("=" * tam)
    print(f"{msg}")
    print("=" * tam)
    sleep(1)


comando = ""

while True:

    título("Sistema de ajuda PyHelp")
    comando = str(input("\nFunção ou Biblioteca > "))

    if comando.upper() == "FIM":
        break

    else:
        ajuda(comando)

título("ATÉ LOGO")
        
