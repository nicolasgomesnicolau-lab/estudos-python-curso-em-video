
#mas tinha q funcionar com virgula é isso










from funções import moeda


p = (input('Digite o preço: R$'))
if "," in p:
    p = float(p.replace(",", "."))
else:
    p = float(p)
au = float(input('fale a porcentagem de aumento pra ver '))
di = float(input('fale a porcentagem de redução pra ver '))
moeda.resumo(p, au, di)