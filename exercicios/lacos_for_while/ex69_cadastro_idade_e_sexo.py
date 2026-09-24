#ler idade e sexo de varias pessoas (infinitas)
#perguntar se o usuario quer continuar ou n
#no final mostrar qnts pessoas mais 18 anos
#qnts homens cadastrados
#e qnts mulheres tem menos de 21 anos :/

#tipo a cada loop é mais uma pessoa registrada saca
#ai a cada registro pergunta se quer continuar

#apenas idade e sexo sem nome
#digitar errado perguntar sexo denovo ou idade sei la

maioridade = 0
homens = 0
mvelha = 0
n = str('oi')

while True:
    idade = int(input('digite sua idade: '))
    if idade > 18:
        maioridade += 1
    sexo = str(input('digite seu sexo [F/M]: ')).upper().strip()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 18:
        mvelha += 1
    cadastro = str(input('Quer cadastrar mais alguem? [S/N]: ')).upper().strip()
    if cadastro == 'N':
        break
print(f'PRONTO, analisando.....\n\nvoce cadastrou exatamente {homens} homens, e tem exatamente {mvelha} mulheres acima dos 18 anos')
