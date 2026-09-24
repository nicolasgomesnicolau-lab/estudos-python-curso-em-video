#funcao maior, que receba parametros indefinidos (*nome)
#e falar qual foi o maior
# 
#aparentemente n tem input vc define no codigo msm
#e denovo com time sleep, e vc faz uma lista de valores ai#

#analisando valores
#valores da lista com time.sleep
#o maior valor foi o maior

#se n tiver maior vc fala q n existe

import time

maior = 0
lista = []

def gigante(valor):
    inicio = valor[0]
    fim = valor[-1]
    print()
    print('-=' * 30)
    print('analisando os valores enviados...')
    for c in range(len(valor)):
        print(valor[c], end=" ", flush=True)
        time.sleep(0.7)
    print(f'foram informados {len(valor)} valores ao todo.')
    print()
    valor.sort()
    maior = valor[-1]
    print(f'o maior valor informado foi...')
    time.sleep(3)
    print(maior)
    print('-=' * 30)

while True:
    valores = int(input('valores: [999 pra parar contagem]: '))
    if valores != 999:
        lista.append(valores)
    if valores == 999:
        gigante(lista)
        sair = str(input('deseja fazer outra vez? [S/N]: '))[0].strip().upper()
        if sair == 'S':
            lista.clear()
            continue
        else:
            break

#o guanabara n usou sort, isso foi meio gambiarra nossa
#ele fez um cont = 0, dps fez o maior ser o primeiro valor
#ai dps do for acabar ele fez cont +=1
#ai se cont fosse maior q zero ele comparava com os ifs
#interessante mas o sort funciona tmb.


#######################################


#algo interessante q descobri foi o comando pass

#tipo literalmente ele n faz nada
#mas ele evita erros, é quase algo pra deixar pra dps
#e continuar o programa sem erros
#se tipo vc faz um if algo e pass embaixo ai n tem erro
#vc continua o codigo


#incluisive é comum programadores só sainda definindo
#funcoes e botando nomes, e variavels com nomes
#e print e tudo mais e colocando pass em tudo
#só pra ir preenchendo dps

#####################################