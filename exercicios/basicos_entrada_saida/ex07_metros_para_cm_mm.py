#Escreva um
#programa que leia um
#valor em metros c o
#cxiba convertido cm
#centimetros @
#milimetros.

m = int(input('digite um valor em metros: '))

cen = int(m * 10)
km = int(m / 1000)

print('vc digitou: {}m\nisso em centimetros da: {}cm!\ne em kilometros da {}km!'.format(m,cen,km))

