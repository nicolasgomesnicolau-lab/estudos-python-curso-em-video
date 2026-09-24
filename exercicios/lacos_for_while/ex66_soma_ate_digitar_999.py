#ler varios numeros inteiros
#só para qnd digitar 999
#no final mostrar quantidade de numeros digitados
#e a soma entre eles
#a soma dos numero valores foi


valores = 0
cont = 0

while True:
    n = int(input('digite seus valores [para parar digite 999]: '))
    if n == 999:
        break
    if n != 999:
        cont += 1
    valores += n
print(f'FIM!!!\n\nvc digitou {cont} valores\ne a soma dos valores foi {valores}')