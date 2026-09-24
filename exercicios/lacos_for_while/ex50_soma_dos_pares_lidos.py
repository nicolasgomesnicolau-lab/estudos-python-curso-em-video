#ler 6 numeros inteiros, com for, e mostre a some somente dos pares com if eu acho


ponto = []
balde = 0

for n in range(1, 7):
    v = int(input('digite um numero inteiro: '))
    if v % 2 == 0:
        balde = balde + v
        ponto.append(v)

print(f'todos os numeros pares foram: {ponto}')

print(f'todos os numeros pares somados dao: {balde}')

#antigamente deu erro pq fiz v = print
#pq eu precisava do v dps pra soma




#pra separar uma informação é o print ainda no laço porem n no tab