#criar no arquivo moedas nas funcoes
#uma funcao chamada resumo()
#q mostre informações geradas pelas funções q ja criamos

#é um continuação do 107 e 108 msm

#ai vc digita o preço normal
#e vai ter o moeda.resumo



#ai aparece, resumo de valor destacado

#ai embaixo
#preço analisado:
#dobro do preço:
#80% de aumento: 
#35% de redução: 
#--------------

from funções import moeda

p = float(input('Digite o preço: R$'))
au = int(input('fale a porcentagem de aumento pra ver '))
di = int(input('fale a porcentagem de redução pra ver '))
moeda.resumo(p, a=au, b=di)