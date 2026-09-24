#ler nome e preço de produtos (infinito)
#perguntar se quer continuar pra cada

#mostrar qnt gastou na compra toda, e qnts custam mais de mil reais
#e o NOME do produto mais barato

soma = 0
barato = 0
mil = 0
mb = 0
cont = 0

while True:
    nome = str(input('digite o nome do produto: ')).upper().strip()
    preço = int(input('digite seu preço: '))
    if preço > 0:
        cont += 1
    if cont == 1:
        barato = preço
        mb = nome
    else:
        if barato > preço:
            barato = preço
            mb = nome
    if preço > 1000:
        mil += 1
    continuar = str(input('quer cadastrar mais um produto? [S/N]: ')).upper().strip()
    soma += preço
    if continuar == 'N':
        break
valor = soma
print(f'PRONTO, analisando.....\n\nvoce gastou exatamente R${valor} nessas compras\nentre os produtos {mil} custaram mais de mil reais\ne o nome do produto mais barato é {mb} que custou R${barato}')