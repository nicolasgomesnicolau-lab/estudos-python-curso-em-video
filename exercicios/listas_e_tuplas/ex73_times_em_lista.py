#mostrar listas de time brasileiros
#os 5 primeiros da listas
#os ultimos 4 tipo zona 
#e times em ordem lfabetica

#e mostrar o time q ta em oitavo

#primeiros 5 colocado
#depois ultimos 4 colocados
#ordem alfabetica
#em q posição esta o cruzeiro

times = ('Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Atlético Mineiro', 
         'Fluminense', 'Grêmio', 'Internacional', 'Cruzeiro', 'Vasco da Gama', 
         'Botafogo', 'Bahia', 'Fortaleza', 'Athletico Paranaense', 'Bragantino', 
         'Cuiabá', 'Atlético Goianiense', 'Criciúma', 'Juventude', 'Vitória')[0:21]

print(f'==========================================================\nos times em ordem das suas posições do campeonato é {times}')

cont = enumerate(times)

#times = times.sort()

for c in times:
    primeiros5 = times[0:6]
    ultimos4 = times[16:21]
    times1 = list(times)
    times1.sort()
    enumerate(times)
print(f'==============================================================================\nos primeiros 5 times da tabela são: {primeiros5}\n========================================\nos 4 times da zona são: {ultimos4}\n========================================\nand the teams on alfabetic order is: {times1}\n======================================')
    #print(enumerate(times))
    #primeiros = times[0:5]
    #ultimos = times[16:21]
    #if times == enumerate(times):
    #    print('deu bom?')
