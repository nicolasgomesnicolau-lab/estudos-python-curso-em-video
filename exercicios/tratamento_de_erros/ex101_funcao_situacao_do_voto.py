#funcao chamada voto
#o parametro vai ser ano dew nascimento da pessoa

#retornando um alor literal indicando se a pessoa
#teve o voto negado, opcional ou obrigatorio

#input(q ano vc nasceu?)
#ai vc faz menos o ano atual
#ai fala o voto idade anos: VOTO (um dos 3)
#com menos de 18 e mais q 16 é opcional
#e com acima de 65 é opcional

def voto(ano):
    from datetime import date
    global atual
    atual = date.today().year
    nascimento = atual - ano
    if nascimento >= 18:
        return f'com {nascimento} anos o voto é OBRIGATORIO'
    if nascimento >= 65:
        return f'com {nascimento} anos o voto NÃO é mais obrigatorio'
    if nascimento >= 16 and nascimento < 18:
        return f'com {nascimento} anos o voto é OPCIONAL'
    if nascimento < 16:
        return f'com {nascimento} anos o voce NÂO pode votar'
nascimento = int(input('em que ano voce nasceu? '))

print(f'{voto(nascimento)}\nano atual: {atual}')

#pra usar o global, vc n pode criar uma variavel nele
#vc cria a variavel com ele dps só mu8da