#input digitar algo entre 1 e 20, mostrar msg se n for entre 1 e 20
#e se ele digitar certo aparece o numero escrito
# bizarro '-'
#dve ter modulo pra isso


lista = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
                    'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 
                    'dezesies', 'dizesete', 'dezoito', 'dezenove', 'vinte')

valor = int(input('digite um valor entre 1 a 20: '))
if valor > 20 and valor > 0:
    print('digite um valor valido')

for c in lista:
    intlista = lista[valor]
print (f'======{intlista}====== é o seu numero em escrito :/'.upper())


#

