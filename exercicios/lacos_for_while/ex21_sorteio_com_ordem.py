#agr ramdom com ordem

import random

aluno1 = input('digite o nome do primeiro aluno: ')
aluno2 = input('digite o nome do primeiro aluno: ')
aluno3 = input('digite o nome do primeiro aluno: ')
aluno4 = input('digite o nome do primeiro aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

r = random.shuffle(alunos)

print (f'a ordem da apresentação de alunos é: {alunos}')