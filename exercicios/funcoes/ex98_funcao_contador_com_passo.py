#funcao chamada contador

#com 3 paramentro (inicio, fim, passo)

#exemplo, inicio 1 até 10, com passo de 1 em 1
#ou 10 ate 1 com passo de 2 em 2

#dps uma personalizada com input

#os exemplos devem ser mostrado com time.sleep
#tipo contagem de 1 ate 10 de 1 em 1, ai vai e no final FIM!

#ai o input é de cada vez tipo inicio:
#fim:
#passo:

#e tem q funcionar com o inicio sendo maior q o fim tmb
#(reberse=True)
#aparentemente tem q funcioanr se o passo foi -1 ou negativo
#ai vc só trasnforma em positivo
#e se for 0 vc coloca pra 1

import time
numeros = []


def contador(inicio, fim, passo):
    print()
    print(f'\bcontagem de {inicio} até {fim} de {passo} em {passo}:')
    if inicio < fim:
        for c in range(inicio, fim+1):
            numeros.append(c)
        if passo > 0:
            certo = numeros[0::passo]
        if passo < 0:
            correto = passo * -1
            certo = numeros[0::correto]
    if inicio > fim:
        arruma = fim * -1
        for c in range(inicio, (arruma-arruma*2)-1, -1):
            numeros.append(c)
        if passo > 0:
            certo = numeros[0::passo]
        if passo < 0:
            correto = passo * -1
            certo = numeros[0::correto]
    for q in range(0, len(certo)):
        print(certo[q], end=" ", flush=True)
        time.sleep(0.5)
    print('FIM!')
    print()
    print('-' * 60)
print(f'contagem de 1 até 10 de 1 em 1: \n')

for c in range(1, 11):
    print(f'{c}', end=" ", flush=True)
    time.sleep(0.3)
print('FIM!')
print()
print('-' * 60)

i= int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))

contador(i, f, p)