#estrturua de repeticao com while
#parte dois da aula de laços

#while aprendemos um pouquinho,
#tem o true pra rodar infinito
#mas basicamente é enquanto condicao verdade 'range infinito' ou enquanto n ter
#resposta q quero loop infinito

#e sobre listas o .append la é pika


#mas ainda n sei estrutura do while

#while not maçã passo no tab e brake

#assim como for range, no while vc usa muito as condiçoes
#no caso do while servem mais como verificações pra passar obstaculos
#if not ele só... segue

#no range era mais pra especificar informações eu acho

#while not, e o if no tab

#e normalmente é while variavel como se fosse condicao msm e coisas no tab

#c = 1

#while c < 10:
#    print(c) #precisa dar a funcao se n ele vai infinito, ele n vai de 0 a 10 só
#    c = c + 1
#print('fim')

n = 1

#while n != 10:
    #n = int(input('digite um valor: '))

#vc precisa colocar algo nos dois pontos se n ele vai infinito bizarro 
#se n rpecisa colocar um balde

#a gente vai precisar de MUITOOOOOOOOOO balde

par = 0
impar = 0
msg = 0

while n != 0:
    n = int(input('digite um numero: '))
    if n >= 0:
        msg += 1
    if n % 2 == 0 and n > 0:
        par = par + 1
    elif n % 2 != 0 and n > 0:
        impar = impar + 1
print(f'vc digitou {par} numeros pares e {impar} numeros impares\ne vc digitou {msg} mensagens')



#precisa de variavel apontando oq vc quer

#random randint q faz escala de 1 a tal

#eu n fazia ideia tipo
#eu quero q ele repita uma acao pra baixo ate 
#chegar a zero n faço ideia de como fazer isso sem o range



#imagine o while como uma roda q gira e so oq ta dentro vai se repetir precisa do numero
#e o menos 1 claro






















#mano while é dificil
#tipo ele n faz nada sozinho em sequencia como o range
#pra fazer ir de variavel a 0
#precisa de uma variavel existente com int
#ai vc da while nela, da print nela e embaixo vc faz a variavel valer ela - 1

#tipo vc precisa construir o loop do zero absoluto, sem outras variaveis apenas usando
#existentes


#tipo o range, ele faz em sequencia bonitinho vc faz um variael + 1
#dai ele ja faz ate o limite imposto la

#no while, vc precisa botar um filtro de onde parar
#eai fazer a variavel evoluir no loop ate ela chegar no pare poh!

#no range vc pode aplicar uns filtros, ver o maior, filtrar as respostas com if
#no while é ate q facil tmb eu acho


#vc precisa alterar a msm variavel tipo é regra praticamente

#pra somar em loops é só fazer um balde receber n, pq dai todos os valores sao somados automatico







#e o while só entende str se uma variavel vlaer ela

#e o while denovo precisa progredir de uma forma q chegue ate o while n sei oq la


#e ai pra informacoes n sei oq ifs blablabla
#ou vc quer acabar ou vc quer informações especificas ou filtragem de respostas

