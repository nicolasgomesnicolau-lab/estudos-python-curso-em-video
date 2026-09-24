#ler varios numeros e colocar na lista(while S/N). dps criar duas listas extras, 
# uma pra par e outro pra impares FDS. ao final mostrar o conteudo das 3 listas.

par = []
impar = []
numlista = []


while True:
    numeros = int(input('digite um numero: '))
    numlista.append(numeros)
    if numeros % 2 == 0:
        par.append(numeros)
    if numeros % 2 != 0:
        impar.append(numeros)
    sair = str(input('deseja continuar? [S/N] ')).upper().strip()
    if sair == 'N':
        print('acabou o programa!\n===========================================')
        break
print(f'aqui estao as suas listas:\nos numeros digitados foram {numlista} \nos numeros pares digitados foram: {par}\nos numeros impares digitados foram: {impar}\n===========================================')