#ler o peso de 5 pessoas e no final mostre o maior e menor peso lido

maiores = 0
menores = 0

for c in range(1, 5):
    peso = int(input(f'digite o peso da {c} pessoa: '))
    if c == 1:
        maiores = peso
        menores = peso
    else:
        if peso > menores:
            maiores = peso
        elif peso < maiores:
            menores = peso
            

print(f'{maiores}, foi o maior peso lido, e {menores} foi o menor peso lido')


#A primeira pessoa chega: Você olha para ela e anota o peso dela. 
# Como não tem mais ninguém para comparar, essa pessoa é, 
# automaticamente, a mais pesada e a mais leve que você viu até agora.



#esse foi o mais dificil
#basicamente vc disse pro c, o primeiro é o maior e menor
#e ai vc fala, se o peso for maior q o menor, ent maiores recebe esse peso
#peso nesse caso é a nova resposta
#o peso é todas as respostas, e o maior e menor, comparam com o primeiro peso
#se for maior substitui

#