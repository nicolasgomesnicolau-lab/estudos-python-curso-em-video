#calcular a soma de todos os numeros impares q sao multiplos de 3 %
#de 1 a 500


balde = 0

for c in range (1, 501):
    if c % 2 != 0:
        balde = balde + c

print(balde)