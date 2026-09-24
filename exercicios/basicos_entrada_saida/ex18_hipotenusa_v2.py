import math

print ('o programa começou')

o = float(input('ddigite o cateto oposto: '))
o1 = o * o
a = float(input('ddigite o cateto adjascente: '))
a1 = a * a

h = o1 + a1
h1 = math.sqrt(h)

print (f'a sua hipotenusa é: {h1:.3}')

#programa nao rodava, tive q colocar print ou n sei se era pq tava vazio a str