#saber menos e maior valor

v = int(input('digite o primeiro valor: '))
v1 = int(input('digite o segundo valor: '))
v2 = int(input('digite o terceiro valor: '))

if v1<v and v2<v:
    print(f'{v} maior numero')
elif v<v1 and v2<v1:
    print(f'{v1} maior numero')
elif v1<v2 and v<v2:
    print(f'{v2} maior numero')

if v1>v and v2>v:
    print(f'{v} menor numero')
elif v>v1 and v2>v1:
    print(f'{v1} menor numero')
elif v1>v2 and v>v2:
    print(f'{v2} menor numero')

#w