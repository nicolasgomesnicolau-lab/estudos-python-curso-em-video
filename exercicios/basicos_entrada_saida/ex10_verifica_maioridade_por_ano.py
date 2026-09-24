dia = input('qual dia uce nasceu zé?: ')
mes = input('qual mes msm?:')
ano = input('e o tal do ano?') 
ano = int (ano)

if ano <= 2007:
    print('vc ta veio eim fih', 
          'ce nasceu no dia:',dia, 'e no mes:',mes,'e ano:',ano)
else:
    print('vc é novin poh tem muita a viver', 
          'ce nasceu no dia: '+dia, 'e no mes:',mes, 'e ano: ',ano)

#ind transofrma informações do input em numeros
#iff precisa desse == ou >= <= btw dois pontos e print em baixo
#virgular tmb no print ou +
# = define valor da variavel ate ent