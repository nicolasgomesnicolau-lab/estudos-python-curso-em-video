#criar codigo q testa se o site pudim.com.br esta acessivel

import requests

url = 'https://pop-lingo.lovable.app/study'
try:
    buscar = requests.get(url)
    print(buscar)
    if buscar.status_code == 200:
        print('achou')
    else:
        print(f'o site {url} nao foi encontrado')
except ValueError:
    pass