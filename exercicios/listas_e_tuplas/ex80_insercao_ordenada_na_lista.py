#usuario digita 5 valores(range) e cadastre na lista,  
# mostrar na ordem crescendo sem usar o sort, 
# ou seja se ele digita 3 e 8 dps 5 vc tem q colocar entre 3 e 8

#o programa tem q ser assim:  
# Digite um valor: 7 Adicionado ao final da lista ... 
# Digite um valor: 2 Adicionado na posição 0 da lista ... 
# Digite um valor: 5 Adicionado na posição 1 da lista ... 
# Digite um valor: 9 Adicionado ao final da lista ... Pigite um valor:


lista = []
maior = 0
menor = 0
cont = 0

for c in range(0, 5):
    valor = int(input('digite um valor: '))
    cont += 1
    if c == 0:
        lista.append(valor)
        maior = valor
        menor = valor
        print('maior valor ate agora no final')

    if maior < valor:
        maior = valor
        lista.append(valor)
        print('adicionado o maior valor')

    if menor > valor:
        menor = valor
        lista.insert(0, valor)
        print('adicionado o menor valor')

    if valor > menor and valor < maior:
        meio = lista.insert(-2, valor)
        print('adicionado no meio da lista')
    if valor > menor and valor < maior and valor > meio:
         acimameio = lista.insert(-3, valor)
    if c == 0 and valor > menor and valor < maior:
        lista.insert(-2, valor)
        print('adicionado no meio da lista')
        
print(f'voce digitou os seguintes numeros: {lista}')