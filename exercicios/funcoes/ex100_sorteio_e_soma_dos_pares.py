#lista chamada numeros vazia provavelmente
# 
# e duas funcoes
# a primeira chamada sorteia
# e a outra chamada soma par
# 
# a primeira sorteia 5(1, 10) numeros
# 
# e a segunda mostra a soma dos valores pares dos sorteados#
#se tiver só um par, ou nenhum par tem q ter o if ai, só temos tal
#ou n temos pares

#denovo com time.sleep, ele sorteando e tal

import random
import time

numeros = []
pares = []


def sorteia():
    soma = 0
    for c in range(0, 5):
        sorteado = random.randint(1, 10)
        numeros.append(sorteado)
        if sorteado % 2 == 0:
            pares.append(sorteado)
            soma = soma + sorteado
        print(numeros[c], end=" ", flush=True)
        time.sleep(0.4)
    print('PRONTO!')
    return soma

soma = sorteia()

def somapar():
    if len(pares) >= 1:
        print(f'os valores pares de {numeros} são:')
    if len(pares) < 1:
        print('pera.. NEM TEM PARES '-'')
    print(pares, end=" ")
    if len(pares) <= 1:
        print('por n ter mais de 1 valor par n da pra somar')
    if len(pares) >= 2:
        print(f'e a soma entre eles é: {soma}')



somapar()


#aqui foi interessante, pq o guanabara n usou return
#ai eu achava q era pra usar e acabei aprendendo ai
#ele fez algo q passou pela minha cabeça mas achei q era
#gambiarra sei la
#ele fez for c in lista
#if par: soma += c

#interessante ja fizemos isso antes e tal mas é legal de se ver

#n pode usar range nessas situacoes pq ele só funciona
#com valores organizados (sort) 
#nesse caso usa apenas o in msm

