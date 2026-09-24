#faça um jogo q o jogo pensa num numero entre 0 e 10 mas ele tenta ate
#acertar, ai timesleep e... ramdomchoice
#e falar qnts vezes ele errou e falar nao a cada erro

import random

n = 1
f = [1, 10]
m =  0
v = 0

while m != n:
    n = int(input('tente acertar um numero entre 1 e 10: '))
    m = random.randint(1, 10)
    if n != m:
        v = v + 1
    print(f'errou era {m} tenta denovo')

print(f'BOAAAAAAA!!!! acertou, vc errou {v} vezes!')