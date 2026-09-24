#funções finalmente

#funcoes e modulos usam parenteses dps do nome



#ele n falou mas acho q o return é pra guarda informações se ila num dicionari
#e... sei la fazer conta tmb
#pra vc chamar ele e isso ser igual a resposta ou conta sei la



#funcoes é simples, vc cria com def
#e chama como se fosse um modulo, nome() as vezes precisando colocar dentro
#e nao colocar qnd vc apenas quer algo especifico sei la



def lin():
    print('-' * 70)

lin()
print('                     meu nome é nicolas ai       ')
lin()
print('     to querendo ficar rico e viajar alguns lugares derrepente       ')
lin()
print('     só quero dinheiro e focar em objetivos pessoais sair daqui   ')
lin()



#isso n funciona pq n tem print
#pra testar funcoes é pra colocar print msm no final da funcao

#-------------------------------------------------------
#def somar(a, b):
#    return a + b

# Você chama a função
#somar(2, 5)
#print(somar)
#--------------------------------------------------------
#pra testar funcoes é pra colocar print msm no final da funcao
#pra testar funcoes é pra colocar print msm no final da funcao
#pra testar funcoes é pra colocar print msm no final da funcao

#ou vc faz a conta no print mas parece cansativo dms





#tmb aparentemente tem variaveis q vc coloca ja no def
#tipo nome(txt) ai em baixo vc coloca a estrutura
#o txt é oq vc digita no () qnd vc chama a funcao

def texto(txt):
    print('-' * 70)
    print(txt)
    print('-' * 70)

texto('                                 opa')

#dentro do () na criacao do df vc basicamente da nome ao q o usuario
#vai usar dentro do parenteses, ai se vc coloca nome, idade
#qnd chama a funcao vc preenche com os dados tendeu
#tipo
# 
def eai(nome, elogio):
    print(f"                    eai {nome} seu {elogio}!")

texto(eai('nicolas', 'sonhador'))

#literalmente pra ver a resposta antes é só colocar o print no lugar
#do q ficaria o RETURN, pq eles sao parecido na forma de montar

#e nao precisa do const em python pq é só guardar numa variavel msm

#e... pra vc importar funcoes q vc criou é só usar o import
#e o nome do arquivo da msm pasta, SIMPLES ASSIM

#tipo ai e comum ter arquivos só de modulos isso é bem interessante





#se na funcao tem duas variaveis no () vc precisa citar eles simples assim


#caso queira poder colocar valores ilimitados no () precisa usar o:
#(*nome) na criação



def contador(*num):
    print(num)

contador(1,4,5,6)


##################

resultado = []

def dobra(lista):
    for c in range(len(lista)):
        dobra = lista[c] * 2
        resultado.append(dobra)
    print(resultado)


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)



#o guanabara usou um while
#ele fez aumentar 1 pra cada iten dalista percorrido
#com uma variavel q ia aumentando
#é bom lembrar q o while precisa de algo q acabe ele,
#seja com um if ou break, if no caso é while mas usar como se fosse if



def somar(*num):
    soma = 0
    for c in num:
        soma += c
    print(f'somando {num} o resultado foi: {soma}')

somar(1,5,7)
somar(76,45,23,43)