#função notas
#pode receber varias notas (*nome)

#e retorna um dicionario com

#qunatidade de notas
#maior nota
#menor nota
#a media da turma
#situação opcional

#e tmb colocar a docstring da funcao pro help
#é pra retornar uma tupla praticamente

#ai colocar outro parametro la de =True
#se for True fala se a situacao foi boa ou ruim
#se for acima de 6 é bom sei la
#entre 5 e 6 é razoavel
#abaixo de 5 fudeu
#abaixo de 3 atacadao ta esperando os crias

#n tem input mas seria legal

registro = []
dicionario = {'total': 0, 'maior': 0, 'menor': 0, 'media': 0}


def notas(*valor):
    pega = 0
    quantidade = len(registro)
    inicio = registro[0]
    for c in registro:
        pega += c
        if c == inicio:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
            if c < menor:
                menor = c
    media = pega // quantidade
    dicionario['total'] = quantidade
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if media > 4 and media < 7:
        dicionario['situação'] = 'razoavel da pra melhorar chefe'
    if media < 5:
        dicionario['situação'] = 'abriu vaga la no atacadão chefe'
    if media > 7 and media < 10:
        dicionario['situação'] = 'OTIMO!'
    if media > 9:
        dicionario['situação'] = 'MEU DEUS, EISTEIN?'
    return dicionario

while True:
    valores = float(input('digite sua nota [999 pra parar]: '))
    if valores > 10 and valores != 999:
        print('ta de brincadeiro amigo? só vale de 10 pra baixo chefe')
        continue
    if valores != 999 and valores < 10:
        registro.append(valores)
    if valores == 999:
        resp = notas(registro)
        break

#guanabaga fez print resp mas quis deixar bonitin ai q lindo

print('-='*30)

for n, i in dicionario.items():
    print(f'{n}: {i}')

#guanabara fez mais curto
#mas ele n fez input
#muito menos while
#ai tive q fazer listas amais, ifs amais alem do while etc

#