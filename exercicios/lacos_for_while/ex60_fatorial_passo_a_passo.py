#ler numero qualquer e mostre o fatorial tipo 5, 5x4,5x3,5x2,5x1
#usa o range primeiro

import math

n = int(input('digite um numero: '))
f = math.factorial(n)
t = n
g = n



#t = valor
#f = resultado fatorial
#mult = 

#eu quero q ele repita uma acao pra baixo ate chegar a zero n faço ideia de 
#como fazer isso sem o range

while t > 2:
    t = t - 1
    guana = f'x {t}'
    g = g * t
    resultado = g
    print(f'{g // t} x {t} = {g}')
print(f'1 e 0 dao {f} tmb ;/\n\no fatorial de {n} é igual a: {f}!!!!!!!')



#esse codigo aqui foi genial o gemini ajudou muito
#primeiro n sabia como fazer de tras pra frente
#mas ai vi q tem q pegar a variavel com valor colocar no while maior q zero
#depois definir a msm variavel com - 1 q é oq importava nesse programa

