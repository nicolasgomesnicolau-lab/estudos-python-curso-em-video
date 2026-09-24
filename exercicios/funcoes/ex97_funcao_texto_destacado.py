#funcao chamada escreva

#vai receber um texto qualquer ai mostra uma mensagem com tamanha adaptavel
#com ----------------
#tipo os traços vao seguir o tamanho do texto


def escreva(texto):
    contar = len(texto) + 8
    print('~' * contar)
    print(f'    {texto}')
    print('~' * contar)

while True:
    enfeite = str(input('digite algo ai pra aparecer bonito: '))
    escreva(enfeite)
    continue