#daptar o desafio 107
#criando uma funcao adicional chamada moeda()
#q consiga mostrar valores como valor monetario

#eentendi foi nadaaaaaaaaa

#aparentemente e é pra deixar de ser float, e colocar RS$ m
#mas direto da funcao

from funções import moeda

v = float(input('digite o preço: R$'))

metade = moeda.metade(v)
dobro = moeda.dobro(v)
aumenta = moeda.aumentar(v)
reduz = moeda.diminuir(v)

print(f'A metade de R${v:.0f} é {moeda.enfeite(metade)}\no dobro de R${v:.0f} é {moeda.enfeite(dobro)}\naumentando 10% de R${v:.0f} temos: {moeda.enfeite(aumenta)}\nreduzindo 13% de R${v:.0f} temos {moeda.enfeite(reduz)}')

#s