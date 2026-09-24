#nome idade e sexo de 4 pessoas no final a media de idade do grupo, 
#o nome do homem mais velho, e qnts mulheres tem menos de 21 anos

maior = 0
nome_velho = 0
mulher_velha = 0
idade = 0

for c in range (1, 4):
    print('=' * 20)
    v = str(input('nome: ')).strip().upper() #tirar espaços e ignorar minusculo ou maiusculo
    b = int(input('idade: '))
    n = str(input('sexo: '))
    
    idade = idade + b
    if c == 1:
        maior = b
        nome_velho = v
    else:
        if b > maior:
            maior = b
            nome_velho = v

    if b >= 18 and n == 'feminino':
        mulher_velha = mulher_velha + 1

media = idade / 3

print(f'a media de idade do grupo é de: {media:.2f}\no nome do homem mais velho é {nome_velho}\ne tem {mulher_velha} mulheres acima dos 18 anos ')

#pra pegar o if como variavel do tab é só usar a variavel q ele menciona

#