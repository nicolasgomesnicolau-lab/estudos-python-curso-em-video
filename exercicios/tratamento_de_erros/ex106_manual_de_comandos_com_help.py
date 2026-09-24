#um mini programa com input e while

#o usuario digita o comando q ele quer saber a funcionalidade
#ai com base nisso vc da help(comando)

#o nome pode ser manual

#e se o usuario digitar "fim" acaba

import time

def manual(comando):
    print('~' * 50)
    print(f'        acessando o manual do comando {comando}    ')
    print('~' * 50)
    time.sleep(1)
    explicação = help(comando)
    return explicação
while True:
    qual = str(input('digite o comando: '))
    if qual != 'fim':
        manual(qual)
    if qual == 'fim' or qual == 'FIM':
        print('~~~~~~~~~~~~~~~\n   ATÉ LOGO!\n~~~~~~~~~~~~~~~')
        break