#fazer listas com produtos, tipo (produto1str, 1, produto2str, 2)
#criar algo em torno de 9 ou 10
#e mostrar na forma tabular tipo, lapis 30 * '.' R$ preço
#com o for parece facil


produtos = ('Arroz 5kg', 25.90, 'Feijão 1kg', 8.50, 
            'Açúcar 1kg', 4.20, 'Óleo de Soja 900ml', 6.80, 'Café 500g', 12.00, 
            'Leite 1L', 5.50, 'Macarrão 500g', 4.00, 'Sal 1kg', 3.50, 
            'Farinha de Trigo 1kg', 5.20, 'Molho de Tomate 300g', 2.80)

print( '='*30, '\n       lista de preços\n','='*30)

soma = 0

for i, valor in enumerate(produtos):
    #soma = i + 1
    if (i + 1) % 2 != 0:
        print(f'{valor}..............................', end=' ')
    if (i + 1) % 2 == 0:
        print('R${:.2f}'.format(valor))