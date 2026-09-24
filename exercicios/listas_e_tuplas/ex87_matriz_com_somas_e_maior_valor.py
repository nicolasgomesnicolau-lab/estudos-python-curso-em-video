#igual ao anterior mas embaixo mostrar:
#a soma dos valores pares
#a soma dos valores da terceira coluna
#e o maior valor da segunda coluna

#as colunas tao sendo contadas como em pé n deitadas

#

linhas = [[], [], []]
pares = 0
pares1 = []
coluna3 = 0
maior = 0

for c in range (1, 10):
    valores = int(input(f'digite o valor {c}: '))
    if valores % 2 == 0:
        pares += valores
        pares1.append(valores)
    if c < 4:
        linhas[0].append(valores)
    if c > 3 and c < 7:
        linhas[1].append(valores)
        if c == 4:
            maior = valores
        if valores > maior and c < 7:
            maior = valores
    if c >= 7:
        linhas[2].append(valores)
        coluna3 = coluna3 + valores
for f in range (0, 3):
    print(f' [ {linhas[0][f]:^5} ] ', end="")
print()
for t in range (0, 3):
    print(f' [ {linhas[1][t]:^5} ] ', end="")
print()
for y in range (0, 3):
    print(f' [ {linhas[2][y]:^5} ] ', end="")
print()

coluna3 = coluna3
print(f'os valores pares foram: {pares1} e a soma entre eles da {pares}\no maior valor da segunda coluna é: {maior} \ne os valores da terceira coluna somados são: {coluna3}')