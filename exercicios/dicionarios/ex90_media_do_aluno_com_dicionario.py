#pedir nome
#ai fala media de nome
#ai o usuario da tmb

#ai vc da print fala qual o nome, qual a media, e se ele foi ou n reprovado

#com dicionarios, se for abaixo de 6 ou 5 reprova
#e n tem loops '-'

dicionario = {'nome': str(input('diga o nome do aluno: ')), 'media': float(input('digite a media do aluno: '))}

print('====================================================================')
print(f'o nome do aluno é {dicionario["nome"]}\na media de {dicionario["nome"]} é {dicionario["media"]}')
if dicionario["media"] < 5:
    print('e ele n passou de ano')
else:
    print('e ele passou de ano!!!!!!!!')