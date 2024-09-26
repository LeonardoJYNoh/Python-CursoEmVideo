#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()

while True:
    nome = input('Nome: ')
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([nome,[nota1, nota2],media])
    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N]').upper().strip()[0]
    if continua == 'N':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, j in enumerate(alunos):
    print(f'{i:<4} {j[0]:<10}{j[2]:>8.1f}')
print('-'*30)

while True:
    num = int(input('Mostrar qual aluno? (999 interrompe: )'))
    if num == 999:
        print('Finalizmando...')
        break
    if 0<= num < len(alunos):
        print(f'Notas do {alunos[num][0]} são {alunos[num][1]}')
    else:
        num = print('Numero invalido, tente novamente')
    print('-'*30)
print('<<< VOLTE SEMPRE >>>')