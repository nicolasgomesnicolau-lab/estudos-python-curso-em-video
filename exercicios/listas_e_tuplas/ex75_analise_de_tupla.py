# ler quatro valores pelo teclado(input)
#final mostra vezees q aparecem 9
#posição q aparece o valor 3
#e mostrar quais eram pares

#tudo na msm tupla

valores = int(input('digite um numero: '))
valores2 = int(input('digite um numero: '))
valores3 = int(input('digite um numero: '))
valores4 = int(input('digite um numero: '))

tuplas = (valores, valores2, valores3, valores4)
ve9 = tuplas.count(9)
ver3 = tuplas.index(3)
cont = 0
print(f'vc digitou os numeros: {tuplas}\no numero 9 aparece {ve9} vezes', end=' ')
if ver3 >= 0:
    print(f'o numero 3 aparece na posição {ver3}')
else: 
    print('o numero tres nao aparece em nenhum iten das tuplas')

for c in tuplas:
    if c % 2 == 0:
        cont += 1
print(f'o numero par aparece {cont} vezes')