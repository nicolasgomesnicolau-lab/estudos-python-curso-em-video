#usar while pra ler varias pessoas

#ler nome, sexo, idade (input)
#quer continuar?

#no fianl mostrar a quantidade de pessoas cadastradas
#a media de idade
#o nome de todas as mulheres cadastradas

#e mostrar o nome das pessoas acima da media de idade, mostrar todos os dados delas
#uma abaixo da outra

cont = 0
media = 0

dicionario = {'mulheres': [], 'acima': [[], [], []], 'comparar': [[], [], []]}

#vc vai precisar fazer conta com, media de idade
#e cont com pessoas acima da media
#dps vc só cadastra

while True:
    nome = str(input('nome: '))
    sexo = str(input('Sexo [M/F]')).strip().upper()
    if sexo == 'F':
        dicionario['mulheres'].append(nome)
    idade = int(input('idade: '))
    media += idade
    sair = str(input('deseja continuar? [S/N]: '))[0].strip().upper()
    cont += 1
    dicionario['comparar'][0].append(nome)
    dicionario['comparar'][1].append(sexo)
    dicionario['comparar'][2].append(idade)
    if sair == 'N':
        break
media = media / cont
dicionario['cadastros'] = cont + 1
dicionario['media'] = media

print(f'=============================================================\nao todo temos {dicionario["cadastros"]} pessoas cadastradas.\na media de idade é de {dicionario["media"]}.\nAs mulheres cadastradas foram {dicionario["mulheres"]}.\nLista das pessoas que estao acima da media:')

print(dicionario['comparar'][2])

for c in range (0, cont):
    if dicionario['comparar'][2][c] > media:
        dicionario['acima'][0].append(dicionario['comparar'][0][c])
        dicionario['acima'][1].append(dicionario['comparar'][1][c])
        dicionario['acima'][2].append(dicionario['comparar'][2][c])
        print(f'nome = {dicionario["acima"][0][-1]}; sexo = {dicionario["acima"][1][-1]}; idade = {dicionario["acima"][2][1]};')