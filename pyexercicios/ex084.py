'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas = list()
dados = list()
max = min = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = min = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continua = ' '
    while continua not in 'SN':
        continua = input('Quer continuar? [S/N] ').upper().strip()
    if continua == 'N':
        break

pesado = list()
leve = list()
for p in pessoas:
    if p[1] == max:
        pesado.append(p[0])
    if p[1] == min:
        leve.append(p[0])

print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {max}Kg. Peso de {pesado}')
print(f'O menor foi de {min}Kg. Peso de {leve}')
