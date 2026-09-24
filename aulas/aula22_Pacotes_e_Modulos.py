#aula de importação de modulos

#e aparentemente é simples

#a unica condição é, precisam estar na msm pasta
#ent... vc cria dois arquivos um calculo outro main
#no calculo tem varias funcoes
#ai no main vc simplesmente faz import calculo

#e com ela vem todas as funcoes
#vc pode falar import nome_da_funcao from calculos tmb

#tmb existe um comando chama as
#pra nomes de arquivos enormes

#vc pode dar import as apelido q vc quer dar

#dai em vez de chamar a biblioteca pelo nome original
#vc chama pelo q vc definiu no as





#######################################################

#praticas q é importante lembrar da programação
#é comum um arquivo inteiro pra funções

#e tmb é comum montar nomes de funcoes e etc
#cobrindo tudo com o pass só pra preencher dps

#e lembre, toos os arquivos sao dtudo funções
#pq oq importa é oq vai pro html,
#ent ele fala pro html tipo
#essa tag vai usar o return dessa funcao
#e essa funcao usa outras funcoes claro
#e... ai o front end enfeita

#( na programação meio q todas os arquivos sao funcoes, 
# e meio q "oq importa" é oq vai pro html? tipo 
# uma tag recebe um return de uma função q as vezes usa 
# outras funcoes e etc, ai o html vai la faz uma tag pra 
# essa informação e o css(front end) pega isso e enfeita?)

#na verdade o return fica num div ou spam aparentemente
#pra poder sumir dps pq vc abre e fecha um div


#(ai dps tem deploy pra nuvem ou repositorio, onde rodam
#scanners e testes, ai talves dps um  ambiente controlado
#pra pentest e etc. e claro no repositorio vc tenta ver erros
#dps vc faz gestao da nuvem


#(ai dps tem deploy pra um repositorio onde rodam testes 
#de segurança pra dai sim ir pra nuvem rodar o site ou 
#dependendo um ambiente controlado onde rode ataques com 
#o site vivo né, é basicamente isso? ai tem a gestão do 
#gogleCloud ou outra nuvem com python etc, pra permissoes 
#alertas etc)

#Código (Dev) ->
#Repositório (Git) ->
#Pipeline (Testes de Segurança/QA) ->
#Nuvem (Deploy/Infraestrutura).
#e claro sem credenciais do codigo e vc adiciona
#nas variavel de ambiente

#ai dps fih, é ingles, pentest, gestao de nuvem
#e aprender js
#e dps protocolos de segurança em codigo ainda
#alem de scanners etc
#=====================================
#-----------
#só talves um palpite de pentest
#basicamente é vc ter permissao pra fazer ou ver dados
#q vc n deveria, por alguma falha no codigo
#ou alguma falha onde vc encontra alguma credencial
#ou senha bruta
#acho q tentar fazer ações com requests
#ou manda codigos(ou requests) se ássando por um...
#por algo q mande no codigo
#e claro... os erros registrados, ver versoes etc
#------------
#mas basicamente sao scanners e protocolo padrão
#dps vc tenta cobrir oq os scanners n cobrem
#e pra vc cobrir oq o scanner n ve,
#basicamente é. vc ver oq ele precisa checar
#e n deixar NENHUM FALHA, ZERO, precisa checar tudo

#pra ser sincero queria ser O PIKA
#isso é interessante pra pentest, vc tem q buscar exeções validas!

#######################################################

#basicamente o guanabara fala
#pra criar um arquivo inteiro so de funcoes
#e importar
#provavelmente vai ficar na msm pasta de aulas mas n sei

#e qnd vc importa um funcao desse arquivo
#vc precisa usar como modulos msm
#nomedoarquivo.nomedafuncao()

#pra n ter q fazer isso pode simplesmente usar o from
#import funcao from uteis
#ou criar uma variavel das funcoes tipo
#funcao1 = arquivo.funcao()

#vc pode usar tmb o from uteis import funcao1, funcao2
#usando virgulas


#----------------------------------------------

#aparentemente da pra separar modulos q vc criou por assuntos
#ou pacotes, tipo um arquivo com varias funcoes
#mas tem algumas q sao do assunto tal
#e n precisa estar na msm pasta, ela pode ta numa subpasta
#de outra coisa tipo pode importar algo no exercicios
#da pasta aulas

#a estrutura de pacires é assim:

#minhas_funcoes/ (uma pasta para guardar seus códigos)

#cores.py

#calculos.py (arquivo com suas funções)


#ai pra chamar é from minhasfuncoes import pacoteespecifico

#-------------------------------------------------


#####################

#acho q vc nem precisa saber oq o modulo faz
#e sim oq ele retorna só isso e quais parametros claro
#isso é bem interessante essa forma de pensar

#as vezes ele nem retorna nada e sim executa algo
#

######################

#só é bom criar variavel com modulos se ela n tem print
#tipo dai aquela variavel vira o return do bagulho
#mas n da pra fazer variavel()








##################








##############