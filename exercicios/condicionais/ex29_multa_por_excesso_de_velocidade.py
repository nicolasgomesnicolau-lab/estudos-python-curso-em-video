#multa carro

c = int(input('digite a velocidade do seu carro: '))

g = 160

h = (c - 80) * 7

if c <= 80:
    print(f'tudo certo chefe vc n ultrapassou o limite de velocidade! q é 80km')
else:
    print(f'\nvc ULTRAPASSOU O LIMITE DE VELOCIDADE!!\nvoce andou {c} por hora e o limite é 80\nvc pagara uma multa de {h}')

#d