#pedir nome: 
#ano de nascimento: 
#carteira de trabalho(0 nao tem): numero da carteira 0 a 4 sei la
#ano de contratação: 
#salario: 

#ai no final mostrar o nome do usuario, idade ctps etc
#tipo mostrar nome: tal, embaixo idade tal blablabla

#mas la embaixo falar ano de aposentadoria (dps de 35 anos de trabalho)

#se o usuario digitar 0 na carteira de trabalha o programa acaba FDS


dicionario = {'nome': str(input('nome: '))}
nascimento = int(input('ano de nascimento: '))
dicionario['carteira'] = int(input('carteira de trabalho (0 não tem): '))
nome = dicionario["nome"]
idade = 2026 - nascimento
carteira = dicionario["carteira"]
if carteira != 0:
    ano = int(input('ano de contratação: '))
    contratação = 2026 - ano
    aposentado = ano + 35 
    salario = int(input('Salario: '))
print(dicionario)
print(f'==================================================================\no nome tem o valor de: {nome}\nidade tem o valor de: {idade}')                                                                          
if dicionario['carteira'] == 0:
    print('carteira de trabalho tem o valor de: nao tem carteira de trabalho')
else:
    print(f'ctps tem o valor de {carteira}\nano de contratação foi em: {ano}\ne trabalha a: {contratação}\nsalario é de: {salario}\ne a aposentadoria vai ser em: {aposentado}')
    
#