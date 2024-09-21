'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

adulto = homens = mulher = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo:  [M/F]').upper().strip()[0] 
    continua = ' '
    if idade >= 18:
        adulto += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    while continua not in 'SN':
        print('-'*30)
        continua = input('Quer continuar? [S/N]').upper().strip()[0]
    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {adulto}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher} mulheres com menso de 20 anos')