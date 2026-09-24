#ler dois valores e mostre o menu na tela
#de 1 a 5, se o usuario clica em 1 soma se em 2 multiplica se em 3 pra saber o maior valor
# 4 pra digitar novos numeros e 5 pra sair do programa

valor1 = int(input(f'digite o primeiro valor: '))
valor2 = int(input('digite o segundo valor: '))

maior1 = 0
c = 0
c1 = 5

while c != c1:
    menu = int(input('[1] somar valores\n[2] multiplicar valores\n[3] ver qual o maior\n[4] digitar novos numeros\n[5] sair do programa\n============================================================\nRESPOSTA: '))
    if menu == 1:
        soma = valor1 + valor2
        print(f'a soma entre os valores da {soma}')
        print('==================================================')
    elif menu == 2:
        multiplicar = valor1 * valor2
        print(f'a multipicação entre os valores é: {multiplicar}')
        print('==================================================')
    elif menu == 3 and valor1 > valor2:
        maior1 = valor1
        print(f'O maior valor digitado foi {maior1}')
        print('==================================================')
    elif menu == 3 and valor2 > valor1:
        maior1 = valor2
        print(f'o maior valor digitado foi {maior1}')
        print('==================================================')
    elif menu == 5:
        c = c + 5
    elif menu == 4:
        valor1 = int(input(f'digite o primeiro valor: '))
        valor2 = int(input('digite o segundo valor: '))

print('vc saiu do jogo foi top né')
