#par ou impar com o computador
#só acaba qnd o jogador perder, e mostrar total de vitorios consecutivos

#digite o valor, ai vc escolhe se quer q o computador bote par ou impar mas é random
#eu acho melhor sem isso de qual vc quer mas blz


import random


cont = 0

while True:
    n = int(input('digite o valor: '))
    computador = random.randint(1, 1000)

    par = 0
    impar = 0

    cpar = 0
    cimpar = 0
    while True:
        if n % 2 == 0:
            par = par + 1
            if par > 1:
                break
        if par > 0:
            print(f'=============================================\no valor escolhido foi {n} e ele é PAR!\ncomputador esta escolhendo...')
        if n % 2 != 0:
            impar = impar + 1
            if impar > 1:
                break
        if impar > 0:
            print(f'=============================================\no valor escolhido foi {n} e ele é IMPAR!\ncomputador esta escolhendo...')
    #
        if computador % 2 == 0:
            print (f'=============================================\nO computador escolheu o numero {computador} que é PAR!!!')
            cpar += 1
            if cpar > 1:
                break
        if computador % 2 != 0:
            print (f'=============================================\nO computador escolheu o numero {computador} que é IMPAR!!!')
            cimpar += 1
            if cimpar > 1:
                break
    if par > 1 and cpar != 1:
        print(f'VOCE PERDEU :/\nporem voce acertou {cont} vezes consecutivas! \nTalves voce tenha mais sorte na proxima!\n=============================================')
        break
    else:
        if par > 1 and cpar == 1:
            cont += 1
            print('VOCE VENCEU!! parabens vamos para a proxima rodada\n=============================================')
    if impar > 1 and cimpar != 1:
        print(f'VOCE PERDEU :/\nporem voce acertou {cont} vezes consecutivas! \nTalves voce tenha mais sorte na proxima!\n=============================================')
        break
    else:
        if impar > 1 and cimpar == 1:
            cont += 1
            print('VOCE VENCEU!! parabens vamos para a proxima rodada\n=============================================')
#top