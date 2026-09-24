#sorteio de alunos
#util

import random

aluno1 = input('digite o nome do primeiro aluno: ')
aluno2 = input('digite o nome do primeiro aluno: ')
aluno3 = input('digite o nome do primeiro aluno: ')
aluno4 = input('digite o nome do primeiro aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

ramdos = random.choice(alunos)

print (f'o aluno sorteado, o azarado da vez foi: \n============{ramdos}==========')