#ler nome de nascimento de sete pessoas
#no final mostrar quais ainda n sao maiores de idade
#e as que sao

#maioriidade = 21


maiores = 0
menores = 0

for c in range (0,7):
    f = (int(input(f'digite o ano de nascimento da pessoa {c}: ')))
    if f >= 21:
        maiores = maiores + 1 
    else: 
        menores = menores + 1
print(f'teve {maiores} maiores de idade e {menores} menores')