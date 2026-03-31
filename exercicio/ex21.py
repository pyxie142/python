from random import choice
alunol = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
lista = [alunol, aluno2, aluno3, aluno4]
escolhido = choice (lista) #escolhe um da lista
print('o aluno escolhido foi {}'.format(escolhido))