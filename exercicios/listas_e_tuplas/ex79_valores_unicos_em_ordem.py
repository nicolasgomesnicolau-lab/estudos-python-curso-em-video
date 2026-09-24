#digitar varios valores numericos(while) e coloca na lista, 
#caso ja tenha vc n adiciona, no final mostrar os valores unicos 
#digitados em ordem crescendo 0 a tal, sempre um quero continuar? S/N
#caso valor ja posto, 'valor duplicado n vou adicionar mas segue o jogo'

lista = []
primeiro = True

while True:
    if primeiro:
        valores1 = int(input('digite um valor: '))
        mesmo = valores1
        lista.append(valores1)
        print('valor adicionado com sucesso...')
        primeiro = False
        while True:
            valores = int(input('digite um valor: '))
            if valores in lista:
                print('valor duplicado n vou adicionar')
            if valores not in lista:
                print('valor adicionado com sucesso...')
                lista.append(valores)
            valores1 = valores
            sair = str(input('Deseja continuar? [S/N] ')).strip().upper()
            if sair == 'N':
                break
    lista.sort()
    print(lista)
    break
