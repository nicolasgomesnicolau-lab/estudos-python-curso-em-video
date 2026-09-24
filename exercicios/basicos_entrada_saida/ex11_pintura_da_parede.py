#ler altura e largura de uma parede em metros, calcular a area, e quantidade de tinta pra pintar
#sendo q cada litro de tinta pinta dois metros quadrados
#qnts litros vai precisar pra pintar a parede todas

a = float(input('digite a altura da parede em metros: '))
l = float(input('digite a largura da parede em metros: '))

area = a * l
litro = 2
tinta = area / 2

print(f'a area da sua parede é: {area}m2\ne voce precisara de {tinta:.1f} litros de tinta pra pinta-la por completo')

