#input nome do jogador:
#quantas nome jogou:
#qnts gol da partida 0: 
#qnts gol na partida 1 (eai vai ate 4) 

#no final mostrar print o nome do jogador é nome
#o historico dele de gols é [mostrar gols do input como lista tipo 0, 2 etc]
#o total de gols dele foi: 
#o nome fez 5 partidas.
#na partida 0 fez (numero de gols do input) gols

#ai mostra todas as partidas de 0 ate 4 (5)

cont = 0

dicionario = {'jogador': str(input('nome do jogador: ')), 'gols': []}
partidas = int(input(f'quantos gols {dicionario['jogador']} jogou? '))
for c in range (0, partidas):
    input_de_gols = int(input(f'quantos gols na partida {c}? '))
    cont += input_de_gols
    dicionario['gols'].append(input_de_gols)
    dicionario['total'] = cont

nome = dicionario['jogador']
total = dicionario['total']
gols = dicionario['gols']


print(f'======================================================\n{dicionario}\n======================================================\no nome do jogador é {nome}\nele fez essa sequencia de gols nas {c + 1} partidas: {gols}\ne fez um total de: {total} gols\n======================================================')
print(f'o jogador {nome} jogou {c + 1} partidas.')
for f in range(0, partidas):
    print(f'na partida {f}, ele fez {dicionario["gols"][f]} gols')
print(f'foi um total de {total} gols')