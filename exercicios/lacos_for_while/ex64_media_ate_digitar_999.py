#ler varios numeros e só para qnt ler 999, no final mostra a quantidade de numeros
#digitados a gente fez isso na aula 14 ja
#mas tem q mostrar a soma entre eles ignorando o 999.
#no final mostra a media entre todos os valores 
#e mostre o menor e maior valores lidos

#s

contador = 0
n = 1
valores = 0
media = 0
soma = 0

while n != 999:
    n = int(input('digite valores ai: '))
    if n != 999:
        contador = contador + 1
        valores = valores + n
        soma = soma + n
media = valores // contador
soma = soma
print(f'ACABOU!!!!!\nVOCE DIGITOU {contador} NUMEROS!!!\na media entre eles é: {media}\na soma entre os valores foram: {soma} ')


#pra somar em loops é só fazer um balde receber n, pq dai todos os valores sao somados automatico