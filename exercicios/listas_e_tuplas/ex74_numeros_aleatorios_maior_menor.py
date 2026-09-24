#gerar 5 numeros aleatorios
#e colocar numa tupla (list)
#depois mostrar a lista dos numeros (aparecer todos)
#e mostrar o menor e o maior valor

import random

maior = 0
menor = 0

for c in range(1, 6):
    sorteio = random.randint(1, 10)
    numeros = (sorteio)
    if c == 1:
        maior = numeros
        menor = numeros
    else:
        if maior < numeros:
            maior = numeros
        if menor > numeros:
            menor = numeros
    print(f'{numeros}', end = ' ')
print(f'foram os valores selecionados!\no maior valor foi o {maior}\ne o menor foi {menor}')