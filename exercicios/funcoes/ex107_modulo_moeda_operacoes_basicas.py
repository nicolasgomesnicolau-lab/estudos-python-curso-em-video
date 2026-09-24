#criar um modulo moeda.py em funcoes
#com as funcoes aumentar, diminuir, dobro e metade

#ai importa e faz os prints

from funções import moeda



v = float(input('Digite o preço: R$'))

print(f'A metade de {v} é {moeda.metade(v)}\nO dobro de {v} é {moeda.dobro(v)}\nAumentando 10%, temos {moeda.aumentar(v)}\nReduzindo 13%, temos {moeda.diminuir(v)}')

#