#simule um caixa eletronico
#coloca cartao, quero sacar quantia, e sai notas disponieis, tipo 20 50
#perguntar qnt ele quer sacar basicamente

#falar quais notas vai entregar, 50 20 10 ou 1 real
#ai tenta ser... eficiente saca

#tipo tantas notas de 50 blablabla
#uma de 20 btw

qnt50 = 0
qnt20 = 0
qnt10 = 0
qnt1 = 0

falta = 1
cont = 0

sacar = int(input('quanto voce deseja sacar: '))


while True:

    if sacar >= 50:
        resto = sacar % 50
        falta = resto
        qnt50 = sacar // 50
        qnt20 = falta // 20
        falta = falta % 20
        if falta >= 10 and falta < 20:
            qnt10 = falta // 10
            resto = falta % 10
            falta = resto
            if falta < 10:
                qnt1 = falta // 1
                resto = falta % 1
                falta = resto
                if falta < 1:
                    break
print(f'para o valor {sacar} voce obteve as seguintes cedulas:\n\ncedulas de 50: {qnt50}\ncedulas de 20: {qnt20}\ncedulas de 10: {qnt10}\ncedular de 1: {qnt1}')
