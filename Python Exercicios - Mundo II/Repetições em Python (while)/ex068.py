import random

cont = 0

print("="*20, "VAMOS JOGAR PAR OU ÍMPAR", "="*20)

while True:

    jogador = str(input("\nQuer par ou impar (P/I)?")).strip().upper()
    n = int(input("Digite um número: "))
    
    pc = random.randint(1, 10)

    total = pc + n

    while jogador not in "PpIi":
         jogador = str(input("\nJogada inválida!!! Escolha par ou impar (P/I)?")).strip().upper()

    if jogador == "P" and total % 2 == 0:

        cont += 1

        print("="*20)

        print(f"Você jogou {n} e o pc jogou {pc}. O total deu: {total}")

        print("Você venceu, vamos jogar novamente...")

        print("="*20)

    elif jogador == "I" and total % 2 != 0:

        cont += 1

        print("="*20)

        print(f"Você jogou {n} e o pc jogou {pc}. O total deu: {total}")

        print("Você venceu, vamos jogar novamente...")

        print("="*20)

    elif total % 2 != 0:

        print("="*20)

        print(f"Você jogou {n} e o pc jogou {pc}. O total deu: {total}")

        print("Você perdeu")

        print("="*20)
        break

    elif total % 2 == 0:

        print("="*20)

        print(f"Você jogou {n} e o pc jogou {pc}. O total deu: {total}")

        print("Você perdeu")
        
        print("="*20)
        break

print(f"Game Over, você venceu {cont} vezes")


    
        







