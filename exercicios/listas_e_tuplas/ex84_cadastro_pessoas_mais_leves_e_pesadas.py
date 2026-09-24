#ler nome de varias pessoas (while) e coloca numa lista
#no final mostrar quantidade de cadastrados
#lista de pessoas mais pesadas
#e uma lista com as mais leves

#pedir nome e peso
#pedir se quer continuar
#ai mostrar as mais pésadas caso tenha duas com o msm peso simples
#e as duas com o menor

#mostrar nmome e peso junto no print

dados = []
primeiro_loop = True
maior = 0
menor = 0
maiormenor = [[], []]
pesonome = []

nomemaior = 0
nomemenor = 0
nomeigualA = 0
nomeigualB = 0

while True:
    dados.append([str(input('digite seu nome: ')), int(input('digite seu peso: '))])
    if dados[0][1] == maior:
        nomeigualA = dados[0][0]
        maiormenor[0].append(nomeigualA)
        print('esse peso é igual ao do maior')
    if dados[0][1] == menor:
        nomeigualB = dados[0][0]
        maiormenor[2].append(nomeigualB)
        print('esse peso é igual ao do menor')
    pesonome.append(dados [:])
    if primeiro_loop == True:
        maior = dados[0][1]
        menor = dados[0][1]
        maiormenor = [[dados[0][0]], [dados[0][1]], [dados[0][0]], [dados[0][1]]]
            #maiores 0 e 1, menores 2 e 3, nome seguido do peso
    sair = str(input('quer continuar?[S/N] ')).upper().strip()
    if sair != int:
        if sair != int and primeiro_loop == False:
            if dados[0][1] > maior:
                maior = dados[0][1]
                nomemaior = dados[0][0]
                maiormenor[1] = [maior]
                maiormenor[0] = [nomemaior]
            if dados[0][1] < menor:
                menor = dados[0][1]
                nomemenor = dados[0][0]
                maiormenor[3] = [menor]
                maiormenor[2] = [nomemenor]
    if sair == 'N':
        break
    dados.clear()
    primeiro_loop = False

print(f'a lista de pessoas cadastraradas foram:\n{pesonome}\n\na pessoa mais pesada digitada foi: {maiormenor[0]} com {maiormenor[1]}Kg\ne a pessoa mais leve foi: {maiormenor[2]} com {maiormenor[3]}Kg')
#print(maiormenor)
#print(maior, menor)


#s
