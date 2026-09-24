#tipo uma sublista mas ao inves de [posicao] vc chama pelo nome msm

#dicionario = {'nome': 'calor'}
#dicionario['nome'] = 'ola' (aqui vc esta alterando)
#dicionario['idade'] = [32, 43] aqui adicionando pq n existe a lista idade
#ai pra chamar é dados["idade"][2] aqui chamando o 3 iten da lista idade dentro do dic

#PRA ADICIONAR n da pra usar append sem o []
#se vc quer adicioanr dps vc precisa fazer
#dicionar = 'nome': [32]
#dicionar['nome'].append(4)


#ou seja pra dicionar é só fazer nome do dicionar[nova lista] = iten
#pra adicionar dentro da lista o iten ja tem q ter o []
#simples e pra mudar é o msm do adicionar mas citando uma lista q ja existe

#ai pra fazer normalmente pode ser:
#dicionario = {}'nome': valornalistanome, 'idade': 25}
#ai pra adicionar mais de uma coisa tem q usar as []




#e tem o dicionario .values() q basicanmente pega apenas os itens
#pra pegar apenas o nome das listas é .key()
#se vc quer os dois é .items()

#da pra fazer isso q é bem interessane:
filme = {'filme': 'star wars', 'ano': '1977', 'diretor': 'george lucas'}
for k, v in filme.items():
    print(f'o {k} é {v}')