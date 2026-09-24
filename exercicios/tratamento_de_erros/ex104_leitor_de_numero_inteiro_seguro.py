#funcao chamada leiaint()

#q vai funcionar como input

#vc chama a funcao assim 
#variavel = funcao('pergunta: ')
#ai a def faz a funcao bizarro

#ai dps da print(vc acabou de digitar numero)

def leiaint(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('\033[31mERRO! DIGITE UM NUMERO INTEIRO.\033[m')
n = leiaint('digite um numero: ')
print(f'voce digitou o numero {n}')


#o try é pra erros né, tipo vc n pode identificar
#erros de sintaxe num if, ai precisa do try
#e o continue é mais pra... whiles no geral
#len tmb é top né
#items tmb, etc
#usava muitos cleans né emfim

#tmb tem o comando finally
#q faz o programa simplesmente rodar idependente de erro

#e o except é sempre com o valueerror

#e o finally serve pra... como um estintor de incendio
#deu erro ent faz isso msm assim

#tmb tem o keyboardinterrupt pra caso o usuario
#aperte control C, dai n da erro



#mas o guanabaras usou o is numeric
#e fez o input ser str

#é uma especie de gambiarra mas ok