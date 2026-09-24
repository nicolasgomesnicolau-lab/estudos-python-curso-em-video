#oq ele ta falando ate agr sao listas dentro de listas com o nome str e unmero int
#e pra printar todos elementos das listas compostas vc tem q chamar [posição]
#e dps chamar o iten ou itens tipo [posição][iten da posição um da sub lista]

##################


#e pra mostrar tudo é só fazer [posição] msm
#e pra algo especifico é lista[posição da sub lista][posição do iten da sub]

#pra dar append e criar uma lista dentro da lista é simples:
#lista.append([itens, itens])
#tipo precisa de um [] dentro do () simples assim

galera = []
dado = []

for c in range (0, 3):
    dado.append(str(input('digite seu nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado [:])
    dado.clear()
print(f'{galera}')