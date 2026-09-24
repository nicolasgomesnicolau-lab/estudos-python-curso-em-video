#função chamada ficha
#q tenha dois parametros oopcionais

#o nome de um é jogador e outro é gols q ele marcou

#ai oprograma tem q mostrar a ficha do jogador msm semdados

#input(nome do jogador
#numeros de gols)

#o jogador tal fez tantos gols no campeonato

#caso n tenha nome, ent desconhecido
#e gols = g gols no camp


#o problema aqui é q... se vc coloca só um valor
#ele vai pro primeiro parametro automatico msm q seja uma 
#informacao q deveria ter ido pro segundo
#a solução é nome_do_segundo_parametro=valor
#ai caso n tenha o primeiro vc só n menciona ele
#genial né


def jogo(jogador='<desconhecido>', gols=0):
    print(f'o jogador {jogador} fez {gols} gol(s) no campeonato')

nome = str(input('nome: '))
try:
    gols = int(input('gol: '))
except ValueError:
    gols = ''

if len(nome) >= 3 and len(gols) >= 1:
    jogo(jogador=nome, gols=gols)
elif len(nome) >= 3 and len(gols) < 1:
    jogo(jogador=nome)
elif len(nome) < 3 and len(gols) < 1:
    jogo()
elif len(nome) < 3 and len(gols) >= 1:
    jogo(gols=gols)

#o guanabara usou o if g.isnumeric()
#mas ele tava na preguisa emfim
