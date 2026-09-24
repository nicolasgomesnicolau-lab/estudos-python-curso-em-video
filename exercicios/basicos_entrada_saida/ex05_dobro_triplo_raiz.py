#Crie um algoritmo
#que leia um numero q
#mostre o seu dobro,
#triplo e raiz quadrada.
#usar f'

n = int(input('digite seu numero: '))
ndobro = int(n * 2)
ntriplo = int(n * 3)
nraiz = float(n ** (1/2))#ou (n ** 0.5)

print(f'o numero digitado foi: {n}\no seu dobro é: {ndobro}\ne seu triplo é: {ntriplo}\ne a sua raiz quadrada é: {nraiz:.2f}')


