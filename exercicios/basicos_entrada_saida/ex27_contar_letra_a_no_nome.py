#relatorio letra a

n = str(input('digite seu nome chefe! ')).strip()

c = n.count('a')
v = n.find('a') +1

w = n.rfind('a') +1

print(f'nome top\nnele existem exatamente {c} A\no primeiro A q aparece é na posição {v}\ne o ultimo A q aparece é na posição {w}')