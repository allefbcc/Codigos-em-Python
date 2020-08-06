import random

aluno1 = input("Informe o primeiro aluno: ")
aluno2 = input("informe o segundo aluno: ")
aluno3 = input ("informe o terceiro aluno: ")
aluno4 = input("informe o quarto aluno: ")

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print("A ordem de sorteio foi: ")
print(lista)
               
