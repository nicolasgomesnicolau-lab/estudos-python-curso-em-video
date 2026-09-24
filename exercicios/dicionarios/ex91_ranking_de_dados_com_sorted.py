#4 jogadores joga um ddo (entre 1 e 6) 
#e tem resultados aleatorios
#guarda tudo em dicionario

#colocar dicionario em ordem.sort sei la

#e falar qm tirou o maior numero (vencedor)

#vai ser isso n tem input:
#com time sleep(2)
#jogador 1 tirou numero entre 1 a 6, e vai ate 4

#ai vc faz o ranking do primeiro ao ultimo lugar
#ent ordem é de maior pro menor
#valores sorteado:
    #jogador um tirou 4

jogador = 'jogador'

dicionario = {'temporarios': 'oi','numeros': []}
dicionario2 = {}
import time
import random
print('sorteando...')
for c in range(0,4):
    for s in range(0, 4):
        sorte = random.randint(1, 6)
    dicionario['temporarios'] = sorte
    dicionario['numeros'].append(sorte)
    dicionario[f'{jogador} {c}'] = (f'com {sorte}')
    print(f'    ----o jogador {c} tirou o numero {dicionario["temporarios"]} no dado')
    time.sleep(0.5)
print('=============================RANKING DOS JOGADORES=============================')

del dicionario['temporarios']
del dicionario['numeros']
for c in range(0, 4):
    ordem = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
for w in range(0, 4):
    print(f'    ----{ordem[w]}')
print('=============================JA ERAS=============================')





##dicionario apenas: jogador, numeros
#nome, item


#e tem o dicionario .values() q basicanmente pega apenas os itens
#pra pegar apenas o nome das listas é .key()
#se vc quer os dois é .items()