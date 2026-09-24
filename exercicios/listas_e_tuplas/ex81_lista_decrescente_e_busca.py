#ler varios numeros e botar na lista(while s/n). Depois disso, mostre:  
# A) Quantos números foram digitados.  
# B) A lista de valoras, ordenada de forma decrescente. maior pro menor reverse 
# C) Se o valor 5 foi digitado e se esta ou n na lista  

#Você digitou 5 elementos. 
#Os valores em ordem decrescente são [9, 5, 3, 2, 0] 
#o valor 5 faz parte da lista!

cont = 0
valores = []



while True:
    numeros = int(input('digite um numero: '))
    cont += 1
    valores.append(numeros)
    sair = str(input('quer continuar? [S/N]')).upper().strip()
    if sair == 'N':
        break
valores.sort(reverse=valores)
cinco = valores.count(5)
print(f'voce digitou {cont} vezes doidera!\nlista sua {valores}\ne o numero 5 aparece {cinco} vezes na sua lista')