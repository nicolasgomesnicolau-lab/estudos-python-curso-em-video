#ler nome e duas notas de varios alunos (while)

#nome primeiro iten, as duas notas o segundo iten (juntas)

#uma lista só ai sublistas

#pergunbtar se quer continuar

#no final mostrar boletim, com nome e media na frente

#ai no final da pra escrever aluno 1 ai aparece o nome e as notas
#pq o boletim é 0 pedro             media

#999 pra interromper

alunos = [[], [], []]

print(alunos[2])
while True:
    nome = str(input('digite o nome do aluno: '))
    nota1 = int(input('primeira nota: '))
    nota2 = int(input('segunda nota: '))
    media = (nota1 + nota2) // 2
    alunos[0].append(nome)
    alunos[1].append(media)
    alunos[2].append([nota1, nota2])
    sair = str(input('quer continuar? [S/N] '))[0].upper().strip()
    if sair == 'N':
        print(f'==========================================\nnumero, nome, media\n==========================================')
        for c in range(0, len(alunos) + 1):
            print(f'{c} {alunos[0][c]:<10}       {alunos[1][c]:>8}')
        mostrar = int(input('mostrar nota de qual aluno?: '))
        print(f'notas de {alunos[0][mostrar]} foi {alunos[2][mostrar]}')
    media = 0