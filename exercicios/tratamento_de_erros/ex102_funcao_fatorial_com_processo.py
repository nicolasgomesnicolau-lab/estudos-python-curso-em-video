#funcao chamada fatorial
#fatorial é multiplicar o numero pelos seus antecessores
#5 = 5x4 5x3 5x2 5x1 = 120

#na funcao vai ter dois parametros, o numero e outro chamado
#show
#q é opcional e se for mostrado vai mostrar o 
#processo de calculo

#aparentemente nem tem input
#mas seria interessante um show sim ou nao

#ele ta falando do comando show=True
#é basicamente um parametro
#q se no print fora vc coloca ele como
#show false ou true ele ativa ou nao um print
#q vc precisa definir dentro da funcao com if é meio feio
#inclusive n precisa ser o nome show=True

#e ele por padrao é false


import math
def fatorial(valor, show=False):
    resultado = math.factorial(valor)
    valor + 1
    texto_processo = ""
    if show == True:
        for c in range(1, valor + 1):
            texto_processo += str(c)
            if c != valor:
                texto_processo += " x "
        texto_processo += f" = {resultado}"
        return texto_processo
    if show == False:
        return resultado

while True:
    valor = int(input('digite o numero que vc quer ver o fatorial: '))
    print(fatorial(valor=valor))
    processo = str(input('deseja ver o processo da conta? [S/N] '))[0].upper().strip()
    if processo == 'S':
        print(fatorial(valor=valor, show=True))
    sair = str(input('deseja fazer com outro numero? [S/N] '))[0].upper().strip()
    if sair == 'N':
        break

#eu tinha feito com print, mas pedi pro gemini
#como q eu daria return na mensagem ele fez algo genial
#na funcao
#aparentemente da pra adicionar string numa string

txt = ""

for p in range(0, 10):
    pstr = str(p)
    txt += pstr
print(txt)

#só txt += p daria erro
#precisa transformar em str antes
#e n da pra fazer antes da soma, só se vc fizer variavel

#caso queira fazer c junto com uma literal string ''
#vc precisa somar separado







#eu tinha simplesmente usado o print mas tava aparecendo 
#none, ai queria q ficasse bonito foi só capricho
#n sabia dessa funcionalidade
#e n sabia q podia usar print tmb o guanabara usou