#digitar numero infinito mas todos pergunta se quer continuar [s/n]
# falar o menor e maior numero denovo '-'
#falar quantidade e media denovo

#n = int(input('digite um valor '))
maior = 1
menor = 1
cont = 1
media = 0
#c = str(input('quer continuar? [S/N] ')).upper


n = str('n').upper
s = str('s').upper
c = s
while c == s:
    n = int(input('digite um valor '))
    c = str(input('quer continuar? [S/N] ')).upper
    if cont == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        elif menor > n:
            menor = n
    if c == s:
        cont = cont + 1
    media = media + n
soma = media // cont
print('fim')
print(f'maior {maior} menor {menor}')
print(f'vc digitou {cont} numeros!\na media dos valores digitados foi {soma}')