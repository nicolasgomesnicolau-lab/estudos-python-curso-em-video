#tuplas com varias palavras
#mostrar cada vogal de cada iten da lita
#tipo na palavra {iten 0 da lista} tem as vogais tal

palavras = ('livro', 'caneta', 'caderno', 'mochila', 
            'janela', 'porta', 'estante', 'tapete', 'espelho', 'quadro')

vogais = ('a', 'e', 'i', 'o', 'u')
#dando 14
i = 0

#print(palavras.index(vogais))

for palavras in palavras:
    print(f'a palavra {palavras} tem as vogais:', end=' ')
    for letras in palavras:
        if letras in vogais:
            print(f'{letras}', end=' ')
    print()
            #if len(letras) == contletras:
                #break
        #if letras == 'a' or letras == 'e' or letras == 'i' or letras == 'o' or letras == 'u':
            #vogal = (letras)
            #print(f'a palavra {palavras} tem as vogais: {vogal}')