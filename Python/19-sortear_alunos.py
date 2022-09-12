from random import choice

aluno1 = str(input("Primeiro aluno(a): "))
aluno2 = str(input("Segundo aluno(a): "))
aluno3 = str(input("Terceiro aluno(a): "))
aluno4 = str(input("Quarto aluno(a): "))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = (choice(lista))
print("Aluno(a) escolhido(a) foi {}".format(sorteado))