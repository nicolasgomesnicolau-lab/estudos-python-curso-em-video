#ler 9 valores
#e mostrar como jogo da velha (matriz)
#tipo [valor] [valor] [valor] ai mais 2 linhas de 3 em baixo

#simples ate, cada valor tem lista talves n sei

fileiras = [[], [], []]

for c in range (1, 10):
    valores = int(input(f'digite o valor {c}: '))
    if c < 4:
        fileiras[0].append(valores)
    if c < 7 and c > 3:
        fileiras[1].append(valores)
    if c >= 7:
        fileiras[2].append(valores)

fileiras0 = fileiras[0][0]

for f in range (0, 3):
    print(f' [ {fileiras[0][f]:^5} ] ', end="")
print()
for t in range (0, 3):
    print(f' [ {fileiras[1][t]:^5} ] ', end="")
print()
for y in range (0, 3):
    print(f' [ {fileiras[2][y]:^5} ] ', end="")
print()
#print(f'[ {fileiras[0][0]} ] [ {fileiras[0][1]} ] [ {fileiras[0][2]} ]\n[ {fileiras[1][0]} ] [ {fileiras[1][1]} ] [ {fileiras[1][2]} ]')