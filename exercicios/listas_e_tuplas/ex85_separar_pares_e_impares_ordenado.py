#ler 7 valores (for) e cadastrar numa lista nessa lista tem duas lstas q separa impar
#e par
#em ordem crescente

#os valores pares digitados foram lista

filtro = [[], []]

for c in range(1, 8):
    valores = int(input(f'digite o {c} valor: '))
    if valores % 2 == 0:
        filtro[0].append(valores)
    else:
        filtro[1].append(valores)
print(f'os valores pares digitados foram: {filtro[0]}\ne os valores impares digitados foram: {filtro[1]}')
