#programa pra ver se é ou nao um numero primo


#balde = 0
num = int(input('digite um numero: '))

for c in range(1, num+1):
    if c % 1 == 0 and num % c == 0:
        print(f'***{float(c)}***')
    else: 
        print(f'{c}')

#tinha dado errado usando num so com o c q deu

#print(balde)

