#titulo controle de terreno embaixo -------

#perguntar largura (m):
#comprimento (m): 

#ai vc basicamentemultiplica os dados
#e fala q a area total é a soma disso ai


print('     controle de terrenos\n-----------------------------')

def area(l, c):
    area = l * c
    print(f'a rea do terreno de largura {l} e comprimento {c} é:\n{area} de area')

largura = float(input('LARGURA (m): '))
comprimento = float(input('comprimento (m): '))

area(largura, comprimento)
