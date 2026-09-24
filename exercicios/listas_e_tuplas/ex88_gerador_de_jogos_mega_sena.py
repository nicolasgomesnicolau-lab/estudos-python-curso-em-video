#ajudar na mega sena
#perguntar qnts jogos
#e vai sortear 6 numeros entre 1 e 60

#perguntar qnts jogos, e ai ele sorteia 4 grupos de 6 jogos 
#cada jogo ele sorteia 6 numeros de 1 e 60

import random  #radint
import time
print(f'=================================jogo da mega sena=================================')
quantos = int(input('qnts jogos vc quer q eu sorteie?: '))
jogos = []
rodadas = []
print('>'*10,'SORTEANDO OS NUMEROS...','<'*10 )
for c in range(0, quantos):
    for r in range(0, 6):
        megasena = random.randint(1, 60)
        rodadas.append(megasena)
    jogos.append(rodadas)
    print(f'jogo {c}: {jogos[c]}')
    time.sleep(1)
    rodadas.clear()
print('PRONTO!')