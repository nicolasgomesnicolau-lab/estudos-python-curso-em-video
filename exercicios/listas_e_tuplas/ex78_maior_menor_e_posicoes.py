#ler 5 valores e guarde em lista, 
# no final mostrar o maior e menor,  e as posições deles
#range 5 claro
#se aparecer o maior valor duas vezes vc tem q falar os dois '-'
#msm vale pro menor

posiçãomaior = 0
posiçãomenor = 0

maior = 0
menor = 0
lista = []

listamaior = [0]
listamenor = [2]
posmaior = 0
posmenor = 0

posiçãomaior = [0]
posiçãomenor = [0]

for pos, c in enumerate(range(0, 5)):
    valores = int(input('digite um valor: '))
    lista.append(valores)
    #posição lista adicionar
    if valores == menor and valores != maior:
        listamenor.append(valores)
        posiçãomenor.append(pos)
    if valores == menor and valores != maior:
        print('esse numero tem o msm valor q o menor atual')
    if valores == maior:
        listamaior.append(valores)
        posiçãomaior.append(pos)
    if valores == maior:
        print('esse numero tem o msm valor q o maior atual')
    #maior menor e posição listas
    if c == 0:
        menor = listamenor[0] = valores
        maior = listamaior[0] = valores
        posmaior = posiçãomaior[0] = pos
        posmenor = posiçãomenor[0] = pos
        print('adicionando o maior iten ate agora...')
    if maior < valores:
        listamaior.clear()
        listamaior.append(valores)
        maior = valores
        posiçãomaior.clear()
        posiçãomaior.append(pos)
        print('adicionando o maior iten ate agora...')
    if menor > valores:
        listamenor.clear()
        listamenor.append(valores)
        posiçãomenor.clear()
        posiçãomenor.append(pos)
        menor = valores
        print('adicionando o menor iten ate agr...')
    if valores != maior and valores != menor:
        print('adicionado a lista')
posmaior = posmaior + 1
posmenor = posmenor + 1
print(f'============================================================\nos numeros digitados foram {lista}\n=======================================================\no valor maior foi: {listamaior} a posição dele é {posiçãomaior}.\no menor foi: {listamenor} ele ta na posição {posiçãomenor}\n=======================================================')
