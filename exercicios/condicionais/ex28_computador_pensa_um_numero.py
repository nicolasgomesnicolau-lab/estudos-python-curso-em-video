#Escreva um programa que fasa o computador "pensar" em um numero inteiro entre
#0 e 5 e pesa para o usuário tentar descobrir qual foi o número ascolhido pelo 
#computador.  O programa daver escrever na tela se o usuário venceu ou perdeu.

from random import choice


p = choice([0, 1, 2, 3, 4, 5])


m = int(input('advinhe qual numero sorteado de um a 5: '))

print('pensando...')

if m == p:
    print(f'parabens vc acertou o numero foi {p} de fato!!!!!!!!!!!!')
elif m >= 6:
    print('amigo eu disse 0 a 5, que resposta é essa :/')
else:
    print(f'infelizmente vc errou\no numero era {p}\n\ntenta de novo ai meu bom 030')


#w