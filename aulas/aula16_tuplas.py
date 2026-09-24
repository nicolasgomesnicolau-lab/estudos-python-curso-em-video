#tuplas, mundo 3 quase no fim :>


#sao algo proximo de listas, o appen é ROUBADO

#é basicamente asssim, variaveis só cabem uma informação
#tuplas cabem mais de uma cabem varias emfim

#nas listas das tuplas, pra chamar vc precisa fazer o fatiamento, tipo... variavel da tupla
#[0](pega o primeiro) ou a posicao especifica caso queira algo especifico
#pra chamar tudo é só chamar a variavel
#caso a tupla seja... de quantidade indefinida vc pode chamar msm assim os numeros
#ou filtrar derrepente, ou usar -1 pro ultimo ou 0 pro ultimo

#e o .appen n funciona em tuplas pq sao imultaveis



#E SUPER IMPORTANTE TUPLAS SAO EM PARENTESES. tipo tupla = (1, 2, 3)

#listas q usam [], e funcionam da msm forma mas vc pode usar o .append(wish add)

#se for 0:10:2 ele pula de dois em dois e ignora o 10 para no 9

#e [0:] vai pra sempre

#e -2 é o penultimo e assim por diante isso é interessante

#e tem o comando len(variavel) ele informa qnts componentes tem na memoria

#atualmente pra fazer de 1 a 10 é usando for c in lista
#se tiver range parenteses lista ele da ERRO n sei pq
#e claro é sequencial tem programas com isso
#e ele acaba qnd a lista acaba sem tem q falar nada


lista = ('python', 'é', 'daora')
for c, p in (enumerate(lista)):
    print(p, c)

#da pra usar for sem range

for f in range(0, len(lista)):
    print(f)
#aqui deu certo o range, ma range precisa sempre de 0 a algo, ent muitas vezes nem é necessario





#normalmente n usa range in tuplas pq.... a tuplas da todos os dados saca
#existe o .count() q serve pra filtrar e mostrar qnts vezes algo especifico apareceu
#e tem o .index() q revela qual posicao o numero q vc botou esta
#se vc usar o index com virgula o segundo valor é o ponto de partida



#mas da pra usar range se vc quiser usar o len, ai por exemplo range 0, len(variavel)
#da pra usar enumerate(variavel) ai ele fala a posição a cada loop



#index() for filter the tuplas and lists




#for é SUPER importante pq ele numera sua lista pra vc poder pegar itens especificos
#ou filtrar ou calcular, ai for cria in variavel ele cria o inicio e final dela ja
#e se vc faz lista[valor do input] ele busca aquele valor na lista coomo posição
#pq [] faz isso


#só da pra filtrar com [] acho q n da pra filtrar com ifs oq seria otimo




#pra vc de fato manipular filtrar e tudo é enumerate lista e colocar 2 variaves no for
#ai a primeira é as posições e vc pode somar filtrar etc



#ODEIO










#importante, pro index funcionar ele tem q ver individualmente os numeros
#eai a gente faz dois for
#um tuplas in tuplas
#dps variavelnova in tuplas

#PROGRAMAÇÂO é isso
#comparação, filtro com if ou loops, atualizar variaveis, e coisas repetitivas ai usa loop
#sempre é, pegar dados(input ou lista ou sei la oq) filtrar os dados e guardar ou exibir

#



#pra fazer tudo ficar alinhado nos prints só usar um print vazio e os outros com end=''

#pra aprofundar as coisas e poder no for vc tem q usar mais de um tipo pra ter caracteres
#ai vc usa os ifs pra n ficar repetindo tipo se tiver em vogal lapa


#dnv, todo for precisa funcionar de forma circular