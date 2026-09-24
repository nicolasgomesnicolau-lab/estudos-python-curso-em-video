#mostrar tabuada de varios numeros um de cada vez pra cara valor digitado pelo usuario
#intorrompido qnd o numero for negativo

#basicamente, mostrar a tabuada, e qnd mostrar mostrar outra e so parar qnd for menos q 0
#tabuada do numero do input


while True:
    dez = 0
    n = int(input('digite um numero pra ver sua tabuada [pra encerrar digite valor negativo]: '))
    if n < 0:
        break
    while True:
        if n >= 0:
            m = dez + 1
            dez = m
            if dez > 10:
                break
        mult = n * dez
        print(f'{n} x {dez} = {mult}')
        if n < 0:
            break

print('programa encerrado volte sempre!')
    

#tmb dava pra fazer com 1 while e um range dentro mas achei q n podia :/
#