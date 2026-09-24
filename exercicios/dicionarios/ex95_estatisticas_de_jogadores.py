#usaw while (quer continuar?)

#pedir nome do jogador
#qnts gols fez na partida 1 dps na 2 ai o quero continuar
#a cada quero continuar o numero de partidas aumenta (fudeu)

#ai mostrar tabela
#numero, nome, gols (lista de gols tipo 0, 2, 3), e o total dps
#{:10>}{:<8}
#ai pedir qual jogador vc quer ver os dados ai ele digita o numero do jogador

#ai print, levantamento do jogador nome(do selecionado)
#no jogo 0 fez gols
#no jogo 1 fez gols

#ai vai ate a qnt de partida q ele fez

#e n para nunca o input de mostrar dados de jogador

#se ele querer um jogador q n existe fala pra tentar novamente

#se digitar 999 para

cont = 0
jogador = 0

d = {'jogador': [], 'carta': [], 'total': [], 'gols': []}

while True:
    nome = str(input('Nome do jogador: '))
    if nome == '' or nome.isnumeric():
        print('vc digitou um valor INVALIDO tente denovo')
        continue
    jogador += 1
    d['jogador'].append(nome)
    partidas = int(input('quantas partidas: '))
    if partidas <= 0:
        print('vc digitou um valor INVALIDO volte')
        continue
    for c in range(0, partidas):
        gols = int(input((f'quantos gols na partida {c}: ')))
        d['carta'].append(gols)
        cont += gols
    d['gols'].append([d['carta'].copy()])
    d['carta'].clear()
    d['total'].append(cont)
    cont = 0
    sair = str(input('quer conctinuar? [S/N]: '))[0 ].upper().strip()
    if sair == 'N':
        break
#listas sao mutaveis ent qnd vc da append numa lista, ela só
#coloca um link na lista q vc ta usando pra copiar
#mas qnd vc da clear o append fica vazio pq é um link n uma copia
#ai precisa do .copy

#LISTAS Q VAMOS USAR:
#JOGADOR, GOLS, TOTAL, TODOS COM POSIÇÃO []
print(len(d["jogador"]))
print('============================================================\nn  nome            gols                total\n------------------------------------------------------\n    ')
for f in range (0, jogador):
    gols1 = str(d['gols'][f])
    print(f'{f} {d["jogador"][f]:<15} {gols1:<20}  {d["total"][f]:>2}')
print('-------------------------------------------------------')
while True:
    dados = int(input('mostrar dados de qual jogador bro? (999 pra parar): '))
    if dados == 999:
        print('>>>>>>>>>>>>ACABOU VOLTE SEMPRE!<<<<<<<<<<<<<<<<<')
        break
    if dados > len(d["jogador"]) - 1:
        print(f'            ERRO, NAO EXISTE JOGADOR NUMERO {dados}')
        continue
    print(f'    --  voce escolheu o jogador {d["jogador"][dados]}:')
    for p in range(len(d["gols"][dados][0])):
        print(f'            no jogo {p} fez {d["gols"][dados][0][p]} gols')