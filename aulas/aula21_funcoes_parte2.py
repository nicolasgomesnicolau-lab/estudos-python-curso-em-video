#funções parte 2
# provavelemnte vai falar de return AI CALICA#

########################################################


#help()
#aparentemente serve pra vc saber oq uma funcao faz
#precisa sempre estar em: ""
#!!!!!!!!!!!!!!!!!!!!!!!
#muito interessante pra modulos
#!!!!!!!!!!!!!!!!!!!!!!!!!!
#e vc pode colocar a sua DEF no help
#pra fazer um DEF seu estar no help é só fazer:
#def nome():
#    """Este é o meu manual."""
#ai ele só executa o nome, e qnd vc chama ele n te mostra 
#isso pq ele n ta num print

help('continue')

#print(dir(modulo q vc importou))
#é um radar q mostra todos os comandos do modulo

import time
print('COMANDOS do TIME')
print(dir(time))

print(f'\n ---------------------------')
help('time.sleep')

#emfim sobre interact help é isso

########################################################

#docstring

#basicamente é a definição do help do seu DEF
#ja falamos sobre isso:
##def nome():
#    """Este é o meu manual."""
#help('nome') fds

#########################################################

#PARAMETREOS OPCIONAIS

#o problema q ele apresentou foi:
#num DEF vc coloca 3 parametros pra soma
#mas se o programador coloca 2 ele da erro
#e agr ele quer burlar isso sem usar (*parametro)

#só colocar =0
#def somar(a, b, c=0):
#isso ja implica num if automatico
#se c n for zero tudo bem, mas se n for colocado parametro
#ele é 0 por natureza

#########################################################

#ESOCOPO DE VARIAVEIS

#foi oq a gente viu no exercicion 100
#se vc cria uma variavel no DEF
#e tentar usar dps n da
#simplesmente pq ela se cria e morre no DEF

#e é por isso q o RETURN existe
#e usamos ele. ele é super importante msm
#ai pra usar apenas os dados do return
#vc cria uma variavel fora do DEF q recebe a funcao
#i = funcao()


#no JS o const é pra isso pra pegar o return
#no python a gente usa variaveis
#o const é como se fosse uma tupla
#e o LET é como se fosse uma variavel comum q vc pode mudar

##########################################################

#ESCOPO GLOBAL e FUNCAO GLOBAL:

#basicamente, se vc cria uma variavel e ela tem um valor x
#msm q vc cria um def acima dela, ela ainda continua valendo
#e nao da ERRO!

#doidera
#!!!!!!!!!!!!!!!!
#global variavel       (fora do DEF) isso elimina
#a necessidade do RETURN
#!!!!!!!!!!!!!!!!!!!

#total = 0
#def somar(a, b):
    #global total
    #total = a + b

############################################################



#importante tmb, as variaveis q carregam funcoes pro
#return, elas sempre chamar as funcoes
#a diferença é q vc guarda o resultado na variavel
#ai vc pode usar print variavel q mostra aresposta daquela 
#em especifico

#aparentemente as funcoes agr n vao ter print

#ent tudo bem chamar pq n chama print nenhum mas 
#ainda chama as funcoes pq elas processam tudo



##########################################################


#tmb tem o True
#caso seja return True

#o if funcao(parametro):
#ja é visto como se for True


##########################################################


#pra usar o global, vc n pode criar uma variavel nele
#vc cria a variavel com ele dps só mu8da