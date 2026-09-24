n = str(input('digite seu nome completo: '))

l = n.lower()
m = n.upper()

p = n.count('')
s = n.split()
p1 = s[0]
c = p1.count('')

print(f'\nseu nome em maiusculo é: {m}\nseu nome em minusculo é: {l}\ne seu nome tem {p-1} letras\nseu primerio nome é {s[0]} e ele tem {c-1} letras')

